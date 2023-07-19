from rest_framework import viewsets, mixins
from rest_framework.generics import ListAPIView
from rest_framework.response import Response as DRFResponse
from .models import ServerStatistics, MapStatistics, MapSizeStatistics, GameModeStatistics, RegionStatistics, DayNightStatistics, AggregatedServerStatistics
from .serializers import AggregatedServerStatisticsSerializer, DayNightStatisticsSerializer, GameModeStatisticsSerializer, MapSizeStatisticsSerializer, MapStatisticsSerializer, RegionStatisticsSerializer, ServerStatisticsSerializer, TotalPlayersAndTimestampSerializer
from django.utils import timezone
from datetime import timedelta
from collections import defaultdict

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
    
class LatestBatchMapStatisticsView(ListAPIView):
    serializer_class = MapStatisticsSerializer

    def get_queryset(self):
        latest_batch_id = MapStatistics.objects.latest('timestamp').batch_id
        return MapStatistics.objects.filter(batch_id=latest_batch_id)

class LatestBatchMapSizeStatisticsView(ListAPIView):
    serializer_class = MapSizeStatisticsSerializer

    def get_queryset(self):
        latest_batch_id = MapSizeStatistics.objects.latest('timestamp').batch_id
        return MapSizeStatistics.objects.filter(batch_id=latest_batch_id)

class LatestBatchGameModeStatisticsView(ListAPIView):
    serializer_class = GameModeStatisticsSerializer

    def get_queryset(self):
        latest_batch_id = GameModeStatistics.objects.latest('timestamp').batch_id
        return GameModeStatistics.objects.filter(batch_id=latest_batch_id)

class LatestBatchRegionStatisticsView(ListAPIView):
    serializer_class = RegionStatisticsSerializer

    def get_queryset(self):
        latest_batch_id = RegionStatistics.objects.latest('timestamp').batch_id
        return RegionStatistics.objects.filter(batch_id=latest_batch_id)

class LatestBatchDayNightStatisticsView(ListAPIView):
    serializer_class = DayNightStatisticsSerializer

    def get_queryset(self):
        latest_batch_id = DayNightStatistics.objects.latest('timestamp').batch_id
        return DayNightStatistics.objects.filter(batch_id=latest_batch_id)

class LatestBatchAggregatedServerStatisticsView(ListAPIView):
    serializer_class = AggregatedServerStatisticsSerializer

    def get_queryset(self):
        latest_batch_id = AggregatedServerStatistics.objects.latest('timestamp').batch_id
        return AggregatedServerStatistics.objects.filter(batch_id=latest_batch_id)

class LastHourGameModeStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        game_mode = self.kwargs['game_mode']
        return GameModeStatistics.objects.filter(timestamp__gte=last_hour_time, name=game_mode).values('timestamp', 'total_players')

class LastHourMapSizeStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        map_size = self.kwargs['map_size']
        return MapSizeStatistics.objects.filter(timestamp__gte=last_hour_time, name=map_size).values('timestamp', 'total_players')

class LastHourMapStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        map_name = self.kwargs['map_name']
        return MapStatistics.objects.filter(timestamp__gte=last_hour_time, name=map_name).values('timestamp', 'total_players')

class LastHourRegionStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        region_name = self.kwargs['region_name']
        return RegionStatistics.objects.filter(timestamp__gte=last_hour_time, name=region_name).values('timestamp', 'total_players')

class LastHourAggregatedServerStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        return AggregatedServerStatistics.objects.filter(timestamp__gte=last_hour_time).values('timestamp', 'total_players')

# Views for overall views 

class LastHourAllRegionsStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        queryset = RegionStatistics.objects.filter(timestamp__gte=last_hour_time)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        statistics_data = defaultdict(list)
        for obj in queryset:
            statistics_data[obj.name].append({
                'timestamp': obj.timestamp,
                'total_players': obj.total_players
            })
        return DRFResponse(statistics_data)
    
class LastHourAllMapsStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        queryset = MapStatistics.objects.filter(timestamp__gte=last_hour_time)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        statistics_data = defaultdict(list)
        for obj in queryset:
            statistics_data[obj.name].append({
                'timestamp': obj.timestamp,
                'total_players': obj.total_players
            })
        return DRFResponse(statistics_data)
    
class LastHourAllMapSizesStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        queryset = MapSizeStatistics.objects.filter(timestamp__gte=last_hour_time)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        statistics_data = defaultdict(list)
        for obj in queryset:
            statistics_data[obj.name].append({
                'timestamp': obj.timestamp,
                'total_players': obj.total_players
            })
        return DRFResponse(statistics_data)
    
class LastHourAllGameModesStatisticsView(ListAPIView):
    serializer_class = TotalPlayersAndTimestampSerializer

    def get_queryset(self):
        last_hour_time = timezone.now() - timedelta(hours=1)
        queryset = GameModeStatistics.objects.filter(timestamp__gte=last_hour_time)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        statistics_data = defaultdict(list)
        for obj in queryset:
            statistics_data[obj.name].append({
                'timestamp': obj.timestamp,
                'total_players': obj.total_players
            })
        return DRFResponse(statistics_data)