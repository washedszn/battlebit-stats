from django.urls import path
from .views import DayNightAggStatisticsViewSet, MapSizeAggStatisticsViewSet, ServerStatisticsViewSet, TimeStatisticsViewSet, GameModeAggStatisticsViewSet, MapAggStatisticsViewSet, RegionAggStatisticsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'server-statistics', ServerStatisticsViewSet, basename='serverstatistics')
router.register(r'time-statistics', TimeStatisticsViewSet, basename='timestatistics')
router.register(r'game-mode-statistics', GameModeAggStatisticsViewSet, basename='gamemodestatistics')
router.register(r'map-statistics', MapAggStatisticsViewSet, basename='mapstatistics')
router.register(r'region-statistics', RegionAggStatisticsViewSet, basename='regionstatistics')
router.register(r'map-size-statistics', MapSizeAggStatisticsViewSet, basename='mapsizestatistics')
router.register(r'day-night-statistics', DayNightAggStatisticsViewSet, basename='daynightstatistics')

urlpatterns = router.urls
