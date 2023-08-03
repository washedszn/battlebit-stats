from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.utils import timezone
from datetime import datetime, timedelta
from .models import PlayerStatistics

class PlayerStatisticsView(View):
    def get(self, request, *args, **kwargs):
        region = kwargs.get('region')
        if 'start_datetime' in kwargs and kwargs['start_datetime']:
            start_datetime = datetime.strptime(kwargs['start_datetime'], '%Y-%m-%d %H:%M:%S')
            start_datetime = start_datetime.replace(minute=0, second=0, microsecond=0)
        else:
            start_datetime = (timezone.now() - timedelta(days=1)).replace(minute=0, second=0, microsecond=0)

        if 'end_datetime' in kwargs and kwargs['end_datetime']:
            end_datetime = datetime.strptime(kwargs['end_datetime'], '%Y-%m-%d %H:%M:%S')
            end_datetime = end_datetime.replace(minute=0, second=0, microsecond=0)
        else:
            end_datetime = timezone.now().replace(minute=0, second=0, microsecond=0)

        # Check if end_datetime exceeds start_datetime by 7 days
        if end_datetime - start_datetime > timedelta(days=7):
            return HttpResponseBadRequest("Range cannot be larger than 7 days")

        if region:
            stats_list = PlayerStatistics.objects.filter(timestamp__range=[start_datetime, end_datetime], region=region)
        else:
            stats_list = PlayerStatistics.objects.filter(timestamp__range=[start_datetime, end_datetime])

        stats_data = []
        for region in stats_list.values_list('region', flat=True).distinct():
            region_stats = stats_list.filter(region=region).order_by('timestamp')
            timestamps = list(region_stats.values_list('timestamp', flat=True))
            min_players = list(region_stats.values_list('min_players', flat=True))
            max_players = list(region_stats.values_list('max_players', flat=True))
            stats_data.append({
                'name': region,
                'timestamps': timestamps,
                'min_players': min_players,
                'max_players': max_players
            })

        return JsonResponse(stats_data, safe=False)
