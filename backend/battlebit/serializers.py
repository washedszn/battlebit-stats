from rest_framework import serializers
from .models import ServerStatistics

class ServerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatistics
        fields = [
            'id', 
            'name', 
            'map', 
            'map_size', 
            'game_mode', 
            'region', 
            'players', 
            'queue_players', 
            'max_players', 
            'hz', 
            'day_night', 
            'is_official', 
            'has_password', 
            'anti_cheat', 
            'build'
        ]
