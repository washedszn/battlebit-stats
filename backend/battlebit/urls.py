from django.urls import path
from .views import PlayerStatisticsView

urlpatterns = [
    path('playerstatistics/<str:start_datetime>/<str:end_datetime>/<str:region>/', PlayerStatisticsView.as_view(), name='player-statistics-date-range-region'),
    path('playerstatistics/<str:start_datetime>/<str:end_datetime>/', PlayerStatisticsView.as_view(), name='player-statistics-date-range'),
    path('playerstatistics/<str:start_datetime>/<str:region>/', PlayerStatisticsView.as_view(), name='player-statistics-date-region'),
    path('playerstatistics/<str:start_datetime>/', PlayerStatisticsView.as_view(), name='player-statistics-date'),
    path('playerstatistics/<str:region>/', PlayerStatisticsView.as_view(), name='player-statistics-region'),
    path('playerstatistics/', PlayerStatisticsView.as_view(), name='player-statistics'),
]
