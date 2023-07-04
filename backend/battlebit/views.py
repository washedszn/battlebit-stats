from rest_framework import viewsets, mixins
from .models import DayNightAggStatistics, GameModeAggStatistics, MapAggStatistics, MapSizeAggStatistics, RegionAggStatistics, ServerStatistics, TimeStatistics
from .serializers import DayNightAggStatisticsSerializer, GameModeAggStatisticsSerializer, MapAggStatisticsSerializer, MapSizeAggStatisticsSerializer, RegionAggStatisticsSerializer, ServerStatisticsSerializer, TimeStatisticsSerializer

class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    pass

class ServerStatisticsViewSet(ReadOnlyModelViewSet):
    queryset = ServerStatistics.objects.all()
    serializer_class = ServerStatisticsSerializer

class TimeStatisticsViewSet(ReadOnlyModelViewSet):
    queryset = TimeStatistics.objects.all()
    serializer_class = TimeStatisticsSerializer

class GameModeAggStatisticsViewSet(ReadOnlyModelViewSet):
    queryset = GameModeAggStatistics.objects.all()
    serializer_class = GameModeAggStatisticsSerializer

class MapAggStatisticsViewSet(ReadOnlyModelViewSet):
    queryset = MapAggStatistics.objects.all()
    serializer_class = MapAggStatisticsSerializer

class RegionAggStatisticsViewSet(ReadOnlyModelViewSet):
    queryset = RegionAggStatistics.objects.all()
    serializer_class = RegionAggStatisticsSerializer

class MapSizeAggStatisticsViewSet(ReadOnlyModelViewSet):
    queryset = MapSizeAggStatistics.objects.all()
    serializer_class = MapSizeAggStatisticsSerializer

class DayNightAggStatisticsViewSet(ReadOnlyModelViewSet):
    queryset = DayNightAggStatistics.objects.all()
    serializer_class = DayNightAggStatisticsSerializer
