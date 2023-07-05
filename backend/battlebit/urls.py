from django.urls import path
from .views import (ServerStatisticsViewSet, LatestBatchMapStatisticsView, LatestBatchMapSizeStatisticsView, LatestBatchGameModeStatisticsView,
                    LatestBatchRegionStatisticsView, LatestBatchDayNightStatisticsView, LatestBatchAggregatedServerStatisticsView)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'server-statistics', ServerStatisticsViewSet, basename='serverstatistics')

urlpatterns = router.urls + [
    path('mapstatistics/latestbatch', LatestBatchMapStatisticsView.as_view(), name='latest-batch-map-stats'),
    path('mapsizestatistics/latestbatch', LatestBatchMapSizeStatisticsView.as_view(), name='latest-batch-map-size-stats'),
    path('gamemodestatistics/latestbatch', LatestBatchGameModeStatisticsView.as_view(), name='latest-batch-game-mode-stats'),
    path('regionstatistics/latestbatch', LatestBatchRegionStatisticsView.as_view(), name='latest-batch-region-stats'),
    path('daynightstatistics/latestbatch', LatestBatchDayNightStatisticsView.as_view(), name='latest-batch-day-night-stats'),
    path('aggregatedserverstatistics/latestbatch', LatestBatchAggregatedServerStatisticsView.as_view(), name='latest-batch-aggregated-stats'),
]
