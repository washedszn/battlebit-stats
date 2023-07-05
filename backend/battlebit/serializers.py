from rest_framework import serializers
from .models import AggregatedServerStatistics, DayNightStatistics, MapStatistics, RegionStatistics, ServerStatistics, MapSizeStatistics, GameModeStatistics

class ServerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatistics
        fields = '__all__'

class MapStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapStatistics
        fields = '__all__'


class MapSizeStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapSizeStatistics
        fields = '__all__'


class GameModeStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModeStatistics
        fields = '__all__'


class RegionStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionStatistics
        fields = '__all__'


class DayNightStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayNightStatistics
        fields = '__all__'


class AggregatedServerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedServerStatistics
        fields = '__all__'
