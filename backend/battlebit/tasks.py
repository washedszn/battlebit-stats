import requests
import uuid
from collections import Counter
from backend.celery import app
from django.utils import timezone
from django.db.models import Min, Max
from datetime import timedelta
from .models import (
    PlayerStatistics,
    ServerStatistics,
    AggregatedServerStatistics,
    DayNightStatistics,
    MapSizeStatistics,
    MapStatistics,
    GameModeStatistics,
    RegionStatistics,
)
from requests import RequestException
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def cleanup_database():
    ServerStatistics.objects.filter(created_at__lt=timezone.now() - timedelta(hours=1)).delete()
    AggregatedServerStatistics.objects.filter(timestamp__lt=timezone.now() - timedelta(hours=1)).delete()
    DayNightStatistics.objects.filter(timestamp__lt=timezone.now() - timedelta(hours=1)).delete()
    MapSizeStatistics.objects.filter(timestamp__lt=timezone.now() - timedelta(hours=1)).delete()
    MapStatistics.objects.filter(timestamp__lt=timezone.now() - timedelta(hours=1)).delete()
    GameModeStatistics.objects.filter(timestamp__lt=timezone.now() - timedelta(hours=1)).delete()
    RegionStatistics.objects.filter(timestamp__lt=timezone.now() - timedelta(hours=1)).delete()


@app.task(bind=True)
def fetch_and_store_data(self):
    try:
        response = requests.get('https://publicapi.battlebit.cloud/Servers/GetServerList', timeout=10)
        response.raise_for_status()  # This will raise an HTTPError if the response was unsuccessful.
    except RequestException as e:  # This catches any requests-related exceptions.
        logger.warning(f"Request failed due to {str(e)}. Not retrying.")
    except Exception as e:  # Catch any other exceptions.
        logger.error(f"An unexpected error occurred: {str(e)}")
    else:
        # Proceed with your data processing
        data = response.json()
        batch_id = uuid.uuid4()
    
        server_stats_list = []
        for item in data:
            server_stats = ServerStatistics(
                batch_id=batch_id,
                name=item.get('Name', 'N/A'),
                map=item.get('Map', 'N/A'),
                map_size=item.get('MapSize', 'N/A'),
                game_mode=item.get('Gamemode', 'N/A'),
                region=item.get('Region', 'N/A'),
                players=item.get('Players', 0),
                queue_players=item.get('QueuePlayers', 0),
                max_players=item.get('MaxPlayers', 0),
                hz=item.get('Hz', 0),
                day_night=item.get('DayNight', 'N/A'),
                is_official=item.get('IsOfficial', False),
                has_password=item.get('HasPassword', False),
                anti_cheat=item.get('AntiCheat', 'N/A'),
                build=item.get('Build', 'N/A'),
            )
            server_stats_list.append(server_stats)
        
        calculate_aggregates(server_stats_list, batch_id)
            
@app.task
def calculate_aggregates(stats, batch_id):
    # Initialize counters
    map_counter = Counter()
    map_size_counter = Counter()
    game_mode_counter = Counter()
    region_counter = Counter()
    day_night_counter = Counter()

    # Initialize player counters
    map_players_counter = Counter()
    map_size_players_counter = Counter()
    game_mode_players_counter = Counter()
    region_players_counter = Counter()
    day_night_players_counter = Counter()

    for stat in stats:
        # Increase counters
        map_counter[stat.map] += 1
        map_size_counter[stat.map_size] += 1
        game_mode_counter[stat.game_mode] += 1
        region_counter[stat.region] += 1
        day_night_counter[stat.day_night] += 1

        # Increase player counters
        map_players_counter[stat.map] += stat.players
        map_size_players_counter[stat.map_size] += stat.players
        game_mode_players_counter[stat.game_mode] += stat.players
        region_players_counter[stat.region] += stat.players
        day_night_players_counter[stat.day_night] += stat.players

    # Create statistics instances
    for map, server_count in map_counter.items():
        MapStatistics.objects.create(
            batch_id=batch_id,
            name=map,
            total_players=map_players_counter[map],
            total_servers=server_count,
        )

    for map_size, server_count in map_size_counter.items():
        MapSizeStatistics.objects.create(
            batch_id=batch_id,
            name=map_size,
            total_players=map_size_players_counter[map_size],
            total_servers=server_count,
        )

    for game_mode, server_count in game_mode_counter.items():
        GameModeStatistics.objects.create(
            batch_id=batch_id,
            name=game_mode,
            total_players=game_mode_players_counter[game_mode],
            total_servers=server_count,
        )

    for region, server_count in region_counter.items():
        RegionStatistics.objects.create(
            batch_id=batch_id,
            name=region,
            total_players=region_players_counter[region],
            total_servers=server_count,
        )

    for day_night, server_count in day_night_counter.items():
        DayNightStatistics.objects.create(
            batch_id=batch_id,
            name=day_night,
            total_players=day_night_players_counter[day_night],
            total_servers=server_count,
        )

@app.task
def update_player_statistics():
    # Get the current datetime with minute, second and microsecond set to 0
    current_timestamp = timezone.now().replace(minute=0, second=0, microsecond=0)

    def update_or_create_statistic(region, min_players, max_players):
        player_statistic, created = PlayerStatistics.objects.get_or_create(
            timestamp=current_timestamp,
            region=region,
            defaults={
                'min_players': min_players,
                'max_players': max_players
            },
        )

        if not created:  # if the object already existed, update min and max if necessary
            if min_players < player_statistic.min_players:
                player_statistic.min_players = min_players
            if max_players > player_statistic.max_players:
                player_statistic.max_players = max_players
            player_statistic.save()

    # Get the minimum and maximum player statistics for each region for the current hour
    region_statistics = RegionStatistics.objects.filter(
        timestamp__hour=current_timestamp.hour
    ).values('name').annotate(
        min_players=Min('total_players'),
        max_players=Max('total_players')
    )

    # Update or create a new PlayerStatistics object for each region
    overall_min_players = 0
    overall_max_players = 0
    for region_statistic in region_statistics:
        region_name = region_statistic['name']
        min_players = region_statistic['min_players']
        max_players = region_statistic['max_players']

        update_or_create_statistic(region_name, min_players, max_players)

        overall_min_players += min_players
        overall_max_players += max_players

    # Update or create a new 'all' record in PlayerStatistics with overall player statistics
    if (overall_max_players != 0 and overall_min_players != 0):
        update_or_create_statistic('All Servers', overall_min_players, overall_max_players)
