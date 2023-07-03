from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServerStatisticsViewSet

router = DefaultRouter()
router.register(r'serverstats', ServerStatisticsViewSet, basename='serverstats')

urlpatterns = [
    path('', include(router.urls)),
]
