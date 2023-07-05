from django.urls import path
from django.http import JsonResponse

from .views import (
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
)

# View to display available API endpoints
def api_overview(request):
    base_url = '/api/battlebit'
    api_urls = {
        'LatestBatchMapStatistics': base_url + '/mapstatistics/latestbatch',
        'LatestBatchMapSizeStatistics': base_url + '/mapsizestatistics/latestbatch',
        'LatestBatchGameModeStatistics': base_url + '/gamemodestatistics/latestbatch',
        'LatestBatchRegionStatistics': base_url + '/regionstatistics/latestbatch',
        'LatestBatchDayNightStatistics': base_url + '/daynightstatistics/latestbatch',
        'LatestBatchAggregatedServerStatistics': base_url + '/aggregatedserverstatistics/latestbatch',
        'LastHourGameModeStatistics': base_url + '/gamemodestatistics/lasthour',
        'LastHourMapSizeStatistics': base_url + '/mapsizestatistics/lasthour',
        'LastHourMapStatistics': base_url + '/mapstatistics/lasthour',
        'LastHourRegionStatistics': base_url + '/regionstatistics/lasthour',
        'LastHourAggregatedServerStatistics': base_url + '/aggregatedserverstatistics/lasthour',
        'ServerStatistics': base_url + '/server-statistics/',
    }
    return JsonResponse(api_urls)

urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('mapstatistics/latestbatch', LatestBatchMapStatisticsView.as_view(), name='latest-batch-map-stats'),
    path('mapsizestatistics/latestbatch', LatestBatchMapSizeStatisticsView.as_view(), name='latest-batch-map-size-stats'),
    path('gamemodestatistics/latestbatch', LatestBatchGameModeStatisticsView.as_view(), name='latest-batch-game-mode-stats'),
    path('regionstatistics/latestbatch', LatestBatchRegionStatisticsView.as_view(), name='latest-batch-region-stats'),
    path('daynightstatistics/latestbatch', LatestBatchDayNightStatisticsView.as_view(), name='latest-batch-day-night-stats'),
    path('aggregatedserverstatistics/latestbatch', LatestBatchAggregatedServerStatisticsView.as_view(), name='latest-batch-aggregated-stats'),
    path('gamemodestatistics/lasthour/<str:region_name>', LastHourGameModeStatisticsView.as_view(), name='last-hour-game-mode-stats'),
    path('mapsizestatistics/lasthour/<str:region_name>', LastHourMapSizeStatisticsView.as_view(), name='last-hour-map-size-stats'),
    path('mapstatistics/lasthour/<str:region_name>', LastHourMapStatisticsView.as_view(), name='last-hour-map-stats'),
    path('regionstatistics/lasthour/<str:region_name>', LastHourRegionStatisticsView.as_view(), name='last-hour-region-stats'),
    path('aggregatedserverstatistics/lasthour/<str:region_name>', LastHourAggregatedServerStatisticsView.as_view(), name='last-hour-aggregated-stats'),
    path('server-statistics/', ServerStatisticsViewSet.as_view({'get': 'list'}), name='serverstatistics'),
]
