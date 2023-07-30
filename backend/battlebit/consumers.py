from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from django.apps import apps
from datetime import timedelta
import json

class StatisticsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.type = self.scope['url_route']['kwargs']['type']
        self.room_group_name = self.type
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # Dynamically set the method for handling updates
        setattr(self, f'{self.type}_update', self.statistics_update)

        await self.accept()
        
        # After accepting connection, send last hour data
        await self.send_last_hour_data()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def statistics_update(self, event):
        # Decode the message content
        content = json.loads(event['text'])

        # Send the content to the client
        await self.send_json(content)

    @database_sync_to_async
    def last_hour_data(self):
        model = apps.get_model('battlebit', self.type)
        last_hour_time = timezone.now() - timedelta(hours=1)
        data = model.objects.filter(timestamp__gte=last_hour_time).values('name', 'timestamp', 'total_players', 'total_servers')
    
        # Group data by game mode name
        grouped_data = {}
        for item in data:
            timestamp = item['timestamp'].astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")  # Convert datetime to string
            if item['name'] in grouped_data:
                grouped_data[item['name']].append({
                    'timestamp': timestamp,
                    'total_players': item['total_players'],
                    'total_servers': item['total_servers']
                })
            else:
                grouped_data[item['name']] = [{
                    'timestamp': timestamp,
                    'total_players': item['total_players'],
                    'total_servers': item['total_servers']
                }]
        return grouped_data

    async def send_last_hour_data(self):
        data = await self.last_hour_data()
        for key, value in data.items():
            message = {
                'name': key,
                'data': value
            }
            await self.send_json(message)

