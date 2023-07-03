import requests
from backend.celery import app
from django.db.models import Count, Avg, Max, Min
from django.utils import timezone
from datetime import timedelta
from .models import (
    ServerStatistics,
    TimeStatistics,
    ServerAggStatistics,
    MapAggStatistics,
    GameModeAggStatistics,
    RegionAggStatistics,
)

@app.task
def fetch_and_store_data():
    response = requests.get('https://publicapi.battlebit.cloud/Servers/GetServerList')
    response.raise_for_status()  
    data = response.json()
    
    # calculate total players
    total_players = sum(item.get('Players', 0) for item in data)

    for item in data:
        server_stats = ServerStatistics(
            name=item.get('Name', 'N/A'),
            map=item.get('Map', 'N/A'),
            map_size=item.get('MapSize', 'N/A'),
            game_mode=item.get('Gamemode', 'N/A'),
            region=item.get('Region', 'N/A'),
            players=item.get('Players', 0),
            total_players=total_players,
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
        
    update_time_statistics.delay()
    update_server_agg_statistics.delay()
    update_map_agg_statistics.delay()
    update_game_mode_agg_statistics.delay()
    update_region_agg_statistics.delay()
        
    # Cleanup old data
    ServerStatistics.objects.filter(created_at__lt=timezone.now() - timedelta(days=7)).delete()

def calculate_and_create_statistics(stats, period):
    # Calculate the aggregates
    avg_players = stats.aggregate(Avg('total_players'))['players__avg']
    most_used_map = stats.values('map').annotate(count=Count('map')).order_by('-count').first()['map']
    most_used_game_mode = stats.values('game_mode').annotate(count=Count('game_mode')).order_by('-count').first()['game_mode']
    most_used_region = stats.values('region').annotate(count=Count('region')).order_by('-count').first()['region']

    # Create the TimeStatistics object
    time_stat = TimeStatistics(
        period=period,
        total_average_players=avg_players,
        most_used_map=most_used_map,
        most_used_game_mode=most_used_game_mode,
        most_used_region=most_used_region,
    )
    time_stat.save()

@app.task
def update_time_statistics():
    # Get statistics for the last hour, day, and 7 days
    last_hour_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(hours=1))
    last_day_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=1))
    last_7_days_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))

    # Calculate and create TimeStatistics objects
    calculate_and_create_statistics(last_hour_stats, "last_hour")
    calculate_and_create_statistics(last_day_stats, "last_day")
    calculate_and_create_statistics(last_7_days_stats, "last_7_days")

def calculate_and_create_agg_statistics(stats, agg_model, group_by_field, primary_key_field, period):
    # Aggregate all servers based on the group_by_field
    grouped_stats = stats.values(group_by_field).annotate(
        total_average_players=Avg('total_players'),
        most_used=Count(group_by_field)
    ).order_by('-most_used')

    # Update the corresponding Aggregate table
    for stat in grouped_stats:
        agg_stat = agg_model.objects.get_or_create(**{
            primary_key_field: stat[group_by_field],
            'period': period
        })

        agg_stat.total_average_players = stat['total_average_players']
        agg_stat.max_players = stat['max_players']
        agg_stat.min_players = stat['min_players']
        agg_stat.save()

@app.task
def update_server_agg_statistics():
    # Get statistics for the last hour, day, and 7 days
    last_hour_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(hours=1))
    last_day_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=1))
    last_7_days_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))

    # Calculate and create Aggregate Statistics objects
    calculate_and_create_agg_statistics(last_hour_stats, ServerAggStatistics, 'name', 'server_name', 'last_hour')
    calculate_and_create_agg_statistics(last_day_stats, ServerAggStatistics, 'name', 'server_name', 'last_day')
    calculate_and_create_agg_statistics(last_7_days_stats, ServerAggStatistics, 'name', 'server_name', 'last_7_days')

@app.task
def update_map_agg_statistics():
    # Get statistics for the last hour, day, and 7 days
    last_hour_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(hours=1))
    last_day_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=1))
    last_7_days_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))

    # Calculate and create Aggregate Statistics objects
    calculate_and_create_agg_statistics(last_hour_stats, MapAggStatistics, 'map', 'map_name', 'last_hour')
    calculate_and_create_agg_statistics(last_day_stats, MapAggStatistics, 'map', 'map_name', 'last_day')
    calculate_and_create_agg_statistics(last_7_days_stats, MapAggStatistics, 'map', 'map_name', 'last_7_days')

@app.task
def update_game_mode_agg_statistics():
    # Get statistics for the last hour, day, and 7 days
    last_hour_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(hours=1))
    last_day_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=1))
    last_7_days_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))

    # Calculate and create Aggregate Statistics objects
    calculate_and_create_agg_statistics(last_hour_stats, GameModeAggStatistics, 'game_mode', 'game_mode_name', 'last_hour')
    calculate_and_create_agg_statistics(last_day_stats, GameModeAggStatistics, 'game_mode', 'game_mode_name', 'last_day')
    calculate_and_create_agg_statistics(last_7_days_stats, GameModeAggStatistics, 'game_mode', 'game_mode_name', 'last_7_days')

@app.task
def update_region_agg_statistics():
    # Get statistics for the last hour, day, and 7 days
    last_hour_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(hours=1))
    last_day_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=1))
    last_7_days_stats = ServerStatistics.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))

    # Calculate and create Aggregate Statistics objects
    calculate_and_create_agg_statistics(last_hour_stats, RegionAggStatistics, 'region', 'region_name', 'last_hour')
    calculate_and_create_agg_statistics(last_day_stats, RegionAggStatistics, 'region', 'region_name', 'last_day')
    calculate_and_create_agg_statistics(last_7_days_stats, RegionAggStatistics, 'region', 'region_name', 'last_7_days')
