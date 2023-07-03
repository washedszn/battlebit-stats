from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServerStatisticsViewSet

router = DefaultRouter()
router.register(r'serverstatistics', ServerStatisticsViewSet, basename='serverstatistics')

urlpatterns = [
    path('', include(router.urls)),
]
