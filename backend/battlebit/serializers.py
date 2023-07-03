from rest_framework import serializers
from .models import ServerStatistics

class ServerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatistics
        fields = ['id', 'server_name', 'active_players', 'max_players']
