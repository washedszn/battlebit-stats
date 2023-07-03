from django.urls import include, path
from rest_framework.routers import DefaultRouter
from battlebit.views import ServerStatisticsViewSet

router = DefaultRouter()
router.register(r'serverstatistics', ServerStatisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]