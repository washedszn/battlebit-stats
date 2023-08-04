from rest_framework import serializers
from .models import PlayerStatistics

class TotalPlayersAndTimestampSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    total_players = serializers.IntegerField()

class PlayerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatistics
        fields = '__all__'