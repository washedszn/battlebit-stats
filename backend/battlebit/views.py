from rest_framework import viewsets
from .models import ServerStatistics
from .serializers import ServerStatisticsSerializer

class ServerStatisticsViewSet(viewsets.ModelViewSet):
    queryset = ServerStatistics.objects.all()
    serializer_class = ServerStatisticsSerializer
