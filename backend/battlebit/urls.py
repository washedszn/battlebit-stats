from django.urls import path
from django.http import JsonResponse

from .views import (
    LastHourAllGameModesStatisticsView,
    LastHourAllMapSizesStatisticsView,
    LastHourAllMapsStatisticsView,
    ServerStatisticsViewSet, 
    LatestBatchMapStatisticsView, 
    LatestBatchMapSizeStatisticsView, 
    LatestBatchGameModeStatisticsView,
    LatestBatchRegionStatisticsView, 
    LatestBatchDayNightStatisticsView, 
    LatestBatchAggregatedServerStatisticsView,
    LastHourGameModeStatisticsView,
    LastHourMapSizeStatisticsView,
    LastHourMapStatisticsView,
    LastHourRegionStatisticsView,
    LastHourAggregatedServerStatisticsView,
    LastHourAllRegionsStatisticsView
)

# View to display available API endpoints
def api_overview(request):
    api_urls = {
        'LatestBatchMapStatistics': '/mapstatistics/latestbatch',
        'LatestBatchMapSizeStatistics': '/mapsizestatistics/latestbatch',
        'LatestBatchGameModeStatistics': '/gamemodestatistics/latestbatch',
        'LatestBatchRegionStatistics': '/regionstatistics/latestbatch',
        'LatestBatchDayNightStatistics': '/daynightstatistics/latestbatch',
        'LatestBatchAggregatedServerStatistics': '/aggregatedserverstatistics/latestbatch',
        'LastHourGameModeStatistics': '/gamemodestatistics/lasthour',
        'LastHourMapSizeStatistics': '/mapsizestatistics/lasthour',
        'LastHourMapStatistics': '/mapstatistics/lasthour',
        'LastHourRegionStatistics': '/regionstatistics/lasthour',
        'LastHourAggregatedServerStatistics': '/aggregatedserverstatistics/lasthour',
        'ServerStatistics': '/server-statistics/',
    }
    return JsonResponse(api_urls)

urlpatterns = [
    path('', api_overview, name='api-overview'),
    # all views for graphs
    path('regionstatistics/lasthour/', LastHourAllRegionsStatisticsView.as_view(), name='last-hour-all-region-stats'),
    path('gamemodestatistics/lasthour/', LastHourAllGameModesStatisticsView.as_view(), name='last-hour-all-game-mode-stats'),
    path('mapsizestatistics/lasthour/', LastHourAllMapSizesStatisticsView.as_view(), name='last-hour-all-map-size-stats'),
    path('mapstatistics/lasthour/', LastHourAllMapsStatisticsView.as_view(), name='last-hour-all-map-stats'),
    # latest batches
    path('mapstatistics/latestbatch', LatestBatchMapStatisticsView.as_view(), name='latest-batch-map-stats'),
    path('mapsizestatistics/latestbatch', LatestBatchMapSizeStatisticsView.as_view(), name='latest-batch-map-size-stats'),
    path('gamemodestatistics/latestbatch', LatestBatchGameModeStatisticsView.as_view(), name='latest-batch-game-mode-stats'),
    path('regionstatistics/latestbatch', LatestBatchRegionStatisticsView.as_view(), name='latest-batch-region-stats'),
    path('daynightstatistics/latestbatch', LatestBatchDayNightStatisticsView.as_view(), name='latest-batch-day-night-stats'),
    path('aggregatedserverstatistics/latestbatch', LatestBatchAggregatedServerStatisticsView.as_view(), name='latest-batch-aggregated-stats'),
    # specific views for graphs
    path('gamemodestatistics/lasthour/<str:game_mode>', LastHourGameModeStatisticsView.as_view(), name='last-hour-game-mode-stats'),
    path('mapsizestatistics/lasthour/<str:map_size>', LastHourMapSizeStatisticsView.as_view(), name='last-hour-map-size-stats'),
    path('mapstatistics/lasthour/<str:map_name>', LastHourMapStatisticsView.as_view(), name='last-hour-map-stats'),
    path('regionstatistics/lasthour/<str:region_name>', LastHourRegionStatisticsView.as_view(), name='last-hour-region-stats'),
    path('aggregatedserverstatistics/lasthour/', LastHourAggregatedServerStatisticsView.as_view(), name='last-hour-aggregated-stats'),
    path('server-statistics/', ServerStatisticsViewSet.as_view({'get': 'list'}), name='serverstatistics'),
]
