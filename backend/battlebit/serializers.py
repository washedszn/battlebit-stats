from rest_framework import serializers
from .models import DayNightAggStatistics, MapSizeAggStatistics, ServerStatistics, TimeStatistics, GameModeAggStatistics, MapAggStatistics, RegionAggStatistics

class ServerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatistics
        fields = '__all__'

class TimeStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStatistics
        fields = '__all__'

class GameModeAggStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModeAggStatistics
        fields = '__all__'

class MapAggStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapAggStatistics
        fields = '__all__'

class RegionAggStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionAggStatistics
        fields = '__all__'
     
class MapSizeAggStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapSizeAggStatistics
        fields = '__all__'

class DayNightAggStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayNightAggStatistics
        fields = '__all__'   