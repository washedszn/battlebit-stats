import uuid
from django.db import models
from django.utils import timezone

PERIOD_CHOICES = [
    ('last_hour', 'Last Hour'),
    ('last_day', 'Last Day'),
    ('last_7_days', 'Last 7 Days'),
]

class ServerStatistics(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    batch_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='N/A')
    map = models.CharField(max_length=50, default='N/A')
    map_size = models.CharField(max_length=50, default='N/A')
    game_mode = models.CharField(max_length=50, default='N/A')
    region = models.CharField(max_length=100, default='N/A')
    players = models.IntegerField(default=0)
    queue_players = models.IntegerField(default=0)
    max_players = models.IntegerField(default=0)
    hz = models.IntegerField(default=0)
    day_night = models.CharField(max_length=50, default='N/A')
    is_official = models.BooleanField(default=False)
    has_password = models.BooleanField(default=False)
    anti_cheat = models.CharField(max_length=50, default='N/A')
    build = models.CharField(max_length=50, default='N/A')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Server Statistic"
        verbose_name_plural = "Server Statistics"
        indexes = [models.Index(fields=['name', 'created_at', 'batch_id'], name='name_date_batch_idx'), ]

    def __str__(self):
        return self.name


class TimeStatistics(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default='last_day')
    total_average_players = models.FloatField(default=0.0)
    most_used_map = models.CharField(max_length=50, default='N/A')
    most_used_game_mode = models.CharField(max_length=50, default='N/A')
    most_used_region = models.CharField(max_length=100, default='N/A')

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Time Statistic"
        verbose_name_plural = "Time Statistics"
        indexes = [models.Index(fields=['timestamp'], name='timestamp_idx'), ]

    def __str__(self):
        return f'{self.get_period_display()} at {self.timestamp}'

class MapAggStatistics(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default='last_day')
    map_name = models.CharField(max_length=50, default='N/A')
    total_average_players = models.FloatField(default=0.0)
    most_used_map_size = models.CharField(max_length=50, default='N/A')
    most_used_day_night = models.CharField(max_length=20, default='N/A')
    most_used_game_mode = models.CharField(max_length=50, default='N/A')
    most_used_region = models.CharField(max_length=100, default='N/A')
    most_used_server = models.CharField(max_length=100, default='N/A')

    class Meta:
        verbose_name = "Map Aggregate Statistic"
        verbose_name_plural = "Map Aggregate Statistics"

    def __str__(self):
        return self.map_name

class GameModeAggStatistics(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default='last_day')
    game_mode_name = models.CharField(max_length=50, default='N/A')
    total_average_players = models.FloatField(default=0.0)
    most_used_map_size = models.CharField(max_length=50, default='N/A')
    most_used_day_night = models.CharField(max_length=20, default='N/A')
    most_used_map = models.CharField(max_length=50, default='N/A')
    most_used_region = models.CharField(max_length=100, default='N/A')
    most_used_server = models.CharField(max_length=100, default='N/A')

    class Meta:
        verbose_name = "Game Mode Aggregate Statistic"
        verbose_name_plural = "Game Mode Aggregate Statistics"

    def __str__(self):
        return self.game_mode_name


class RegionAggStatistics(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default='last_day')
    region_name = models.CharField(max_length=100, default='N/A')
    total_average_players = models.FloatField(default=0.0)
    most_used_map_size = models.CharField(max_length=50, default='N/A')
    most_used_day_night = models.CharField(max_length=20, default='N/A')
    most_used_map = models.CharField(max_length=50, default='N/A')
    most_used_game_mode = models.CharField(max_length=50, default='N/A')
    most_used_server = models.CharField(max_length=100, default='N/A')

    class Meta:
        verbose_name = "Region Aggregate Statistic"
        verbose_name_plural = "Region Aggregate Statistics"

    def __str__(self):
        return self.region_name

class MapSizeAggStatistics(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default='last_day')
    map_size_name = models.CharField(max_length=50, default='N/A')
    total_average_players = models.FloatField(default=0.0)
    most_used_day_night = models.CharField(max_length=20, default='N/A')
    most_used_map = models.CharField(max_length=50, default='N/A')
    most_used_game_mode = models.CharField(max_length=50, default='N/A')
    most_used_region = models.CharField(max_length=100, default='N/A')
    most_used_server = models.CharField(max_length=100, default='N/A')

    class Meta:
        verbose_name = "Map Size Aggregate Statistic"
        verbose_name_plural = "Map Size Aggregate Statistics"

    def __str__(self):
        return self.map_size


class DayNightAggStatistics(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default='last_day')
    day_night_name = models.CharField(max_length=20, choices=[('Day', 'Day'), ('Night', 'Night')], default='Day')
    total_average_players = models.FloatField(default=0.0)
    most_used_map_size = models.CharField(max_length=50, default='N/A')
    most_used_map = models.CharField(max_length=50, default='N/A')
    most_used_game_mode = models.CharField(max_length=50, default='N/A')
    most_used_region = models.CharField(max_length=100, default='N/A')
    most_used_server = models.CharField(max_length=100, default='N/A')

    class Meta:
        verbose_name = "Day/Night Aggregate Statistic"
        verbose_name_plural = "Day/Night Aggregate Statistics"

    def __str__(self):
        return self.day_night
