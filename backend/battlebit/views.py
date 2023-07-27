from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from datetime import datetime, timedelta
from .models import PlayerStatistics

class PlayerStatisticsView(View):
    def get(self, request, *args, **kwargs):
        # Check if start_datetime is a datetime string or region
        try:
            start_datetime = datetime.strptime(kwargs.get('start_datetime', ''), '%Y-%m-%d %H:%M:%S')
            region = kwargs.get('region')
        except ValueError:
            start_datetime = timezone.now() - timedelta(days=1)
            region = kwargs.get('start_datetime')

        if 'end_datetime' in kwargs and kwargs['end_datetime']:
            end_datetime = datetime.strptime(kwargs['end_datetime'], '%Y-%m-%d %H:%M:%S')
        else:
            end_datetime = timezone.now()  # get data up to now if end_datetime is not given

        if region:
            stats_list = PlayerStatistics.objects.filter(timestamp__range=[start_datetime, end_datetime], region=region)
        else:
            stats_list = PlayerStatistics.objects.filter(timestamp__range=[start_datetime, end_datetime])

        stats_data = []
        for region in stats_list.values_list('region', flat=True).distinct():
            region_stats = stats_list.filter(region=region)
            min_players = list(region_stats.values_list('min_players', flat=True))
            max_players = list(region_stats.values_list('max_players', flat=True))
            stats_data.append({
                'name': region,
                'start_date': start_datetime,
                'end_date': end_datetime,
                'min_players': min_players,
                'max_players': max_players
            })

        return JsonResponse(stats_data, safe=False)
