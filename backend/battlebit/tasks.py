import requests
import uuid
from collections import Counter
from backend.celery import app
from django.utils import timezone
from datetime import timedelta
from .models import (
    ServerStatistics,
    AggregatedServerStatistics,
    DayNightStatistics,
    MapSizeStatistics,
    MapStatistics,
    GameModeStatistics,
    RegionStatistics
)

@app.task
def fetch_and_store_data():
    response = requests.get('https://publicapi.battlebit.cloud/Servers/GetServerList')
    response.raise_for_status()  
    data = response.json()
    
    batch_id = uuid.uuid4()
    
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
        server_stats.save()
        
    calculate_aggregates(batch_id)
        
    # 1 hour server stat cleanup
    ServerStatistics.objects.filter(created_at__lt=timezone.now() - timedelta(hours=1)).delete()
    # 1 hour aggregate cleanup
    AggregatedServerStatistics.objects.filter(timestamp=timezone.now() - timedelta(hours=1)).delete()
    DayNightStatistics.objects.filter(timestamp=timezone.now() - timedelta(hours=1)).delete()
    MapSizeStatistics.objects.filter(timestamp=timezone.now() - timedelta(hours=1)).delete()
    MapStatistics.objects.filter(timestamp=timezone.now() - timedelta(hours=1)).delete()
    GameModeStatistics.objects.filter(timestamp=timezone.now() - timedelta(hours=1)).delete()
    RegionStatistics.objects.filter(timestamp=timezone.now() - timedelta(hours=1)).delete()

@app.task
def calculate_aggregates(batch_id):
    stats = ServerStatistics.objects.filter(batch_id=batch_id)

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
    
    # Find the most and least common for each counter
    most_used_map, most_used_map_count = map_counter.most_common(1)[0]
    least_used_map, least_used_map_count = map_counter.most_common()[-1]
    
    most_used_map_size, most_used_map_size_count = map_size_counter.most_common(1)[0]
    least_used_map_size, least_used_map_size_count = map_size_counter.most_common()[-1]
    
    most_used_game_mode, most_used_game_mode_count = game_mode_counter.most_common(1)[0]
    least_used_game_mode, least_used_game_mode_count = game_mode_counter.most_common()[-1]
    
    most_used_region, most_used_region_count = region_counter.most_common(1)[0]
    least_used_region, least_used_region_count = region_counter.most_common()[-1]
    
    most_common_time_of_day, most_common_time_of_day_count = day_night_counter.most_common(1)[0]
    least_common_time_of_day, least_common_time_of_day_count = day_night_counter.most_common()[-1]
    
    # Create the aggregate statistics object
    agg_stats = AggregatedServerStatistics(
        batch_id=batch_id,
        
        total_players=sum(map_players_counter.values()),
        total_maps=len(map_counter),
        total_regions=len(region_counter),
        total_map_sizes=len(map_size_counter),
        
        most_used_map=most_used_map,
        most_used_map_count=most_used_map_count,
        most_used_map_total_players=map_players_counter[most_used_map],
        
        least_used_map=least_used_map,
        least_used_map_count=least_used_map_count,
        least_used_map_total_players=map_players_counter[least_used_map],
        
        most_used_map_size=most_used_map_size,
        most_used_map_size_count=most_used_map_size_count,
        most_used_map_size_total_players=map_size_players_counter[most_used_map_size],
        
        least_used_map_size=least_used_map_size,
        least_used_map_size_count=least_used_map_size_count,
        least_used_map_size_total_players=map_size_players_counter[least_used_map_size],
        
        most_used_game_mode=most_used_game_mode,
        most_used_game_mode_count=most_used_game_mode_count,
        most_used_game_mode_total_players=game_mode_players_counter[most_used_game_mode],
        
        least_used_game_mode=least_used_game_mode,
        least_used_game_mode_count=least_used_game_mode_count,
        least_used_game_mode_total_players=game_mode_players_counter[least_used_game_mode],
        
        most_used_region=most_used_region,
        most_used_region_count=most_used_region_count,
        most_used_region_total_players=region_players_counter[most_used_region],
        
        least_used_region=least_used_region,
        least_used_region_count=least_used_region_count,
        least_used_region_total_players=region_players_counter[least_used_region],
        
        most_common_time_of_day=most_common_time_of_day,
        most_common_time_of_day_count=most_common_time_of_day_count,
        most_common_time_of_day_total_players=day_night_players_counter[most_common_time_of_day],
        
        least_common_time_of_day=least_common_time_of_day,
        least_common_time_of_day_count=least_common_time_of_day_count,
        least_common_time_of_day_total_players=day_night_players_counter[least_common_time_of_day],
    )
    agg_stats.save()