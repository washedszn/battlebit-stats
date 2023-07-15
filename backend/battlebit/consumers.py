from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from datetime import timedelta
import json

class GameModeStatisticsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'gamemodestatistics'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        # After accepting connection, send last hour data
        await self.send_last_hour_data()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def gamemodestatistics_update(self, event):
        # Decode the message content
        content = json.loads(event['text'])

        # Send the content to the client
        await self.send_json(content)

    @database_sync_to_async
    def last_hour_data(self):
        from .models import GameModeStatistics
        last_hour_time = timezone.now() - timedelta(hours=1)
        data = GameModeStatistics.objects.filter(timestamp__gte=last_hour_time).values('name', 'timestamp', 'total_players')
    
        # Group data by game mode name
        grouped_data = {}
        for item in data:
            timestamp = item['timestamp'].strftime('%Y-%m-%dT%H:%M:%S')  # Convert datetime to string
            if item['name'] in grouped_data:
                grouped_data[item['name']].append({
                    'timestamp': timestamp,
                    'total_players': item['total_players']
                })
            else:
                grouped_data[item['name']] = [{
                    'timestamp': timestamp,
                    'total_players': item['total_players']
                }]
        return grouped_data

    async def send_last_hour_data(self):
        data = await self.last_hour_data()
        await self.send_json(data)

