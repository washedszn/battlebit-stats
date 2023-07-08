import uuid
from django.db import models
from django.utils import timezone

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

class AggregatedServerStatistics(models.Model):
    # Assuming each aggregation is based on a unique batch and timestamp
    batch_id = models.UUIDField(default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Fields for overall statistics
    total_players = models.IntegerField(default=0)
    total_maps = models.IntegerField(default=0)
    total_regions = models.IntegerField(default=0)
    total_map_sizes = models.IntegerField(default=0)

    # Fields for map statistics
    most_used_map = models.CharField(max_length=100)
    most_used_map_count = models.IntegerField(default=0)
    most_used_map_total_players = models.IntegerField(default=0)

    least_used_map = models.CharField(max_length=100)
    least_used_map_count = models.IntegerField(default=0)
    least_used_map_total_players = models.IntegerField(default=0)

    # Fields for map_size statistics
    most_used_map_size = models.CharField(max_length=100)
    most_used_map_size_count = models.IntegerField(default=0)
    most_used_map_size_total_players = models.IntegerField(default=0)

    least_used_map_size = models.CharField(max_length=100)
    least_used_map_size_count = models.IntegerField(default=0)
    least_used_map_size_total_players = models.IntegerField(default=0)

    # Fields for game_mode statistics
    most_used_game_mode = models.CharField(max_length=100)
    most_used_game_mode_count = models.IntegerField(default=0)
    most_used_game_mode_total_players = models.IntegerField(default=0)

    least_used_game_mode = models.CharField(max_length=100)
    least_used_game_mode_count = models.IntegerField(default=0)
    least_used_game_mode_total_players = models.IntegerField(default=0)

    # Fields for region statistics
    most_used_region = models.CharField(max_length=100)
    most_used_region_count = models.IntegerField(default=0)
    most_used_region_total_players = models.IntegerField(default=0)

    least_used_region = models.CharField(max_length=100)
    least_used_region_count = models.IntegerField(default=0)
    least_used_region_total_players = models.IntegerField(default=0)

    # Fields for day_night statistics
    most_common_time_of_day = models.CharField(max_length=50)
    most_common_time_of_day_count = models.IntegerField(default=0)
    most_common_time_of_day_total_players = models.IntegerField(default=0)

    least_common_time_of_day = models.CharField(max_length=50)
    least_common_time_of_day_count = models.IntegerField(default=0)
    least_common_time_of_day_total_players = models.IntegerField(default=0)

    class Meta:
        # Ensure uniqueness on period and timestamp
        unique_together = ['batch_id', 'timestamp']
    
class BaseStatistics(models.Model):
    batch_id = models.UUIDField(default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    total_players = models.IntegerField(default=0)
    total_servers = models.IntegerField(default=0)

    class Meta:
        abstract = True
        unique_together = ['batch_id', 'timestamp', 'name']
        ordering = ['-timestamp'] # newest to oldest ordering

class RegionStatistics(BaseStatistics):
    pass

class MapStatistics(BaseStatistics):
    pass

class MapSizeStatistics(BaseStatistics):
    pass

class GameModeStatistics(BaseStatistics):
    pass

class DayNightStatistics(BaseStatistics):
    pass