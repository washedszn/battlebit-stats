import requests
from backend.celery import app
from .models import ServerStatistics

@app.task
def fetch_and_store_data():
    response = requests.get('https://publicapi.battlebit.cloud/Servers/GetServerList')
    response.raise_for_status()  # Optional, but good practice to ensure a valid response
    data = response.json()
    for item in data:
        server_stats = ServerStatistics(
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
