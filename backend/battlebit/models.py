from django.db import models
from django.utils import timezone

class ServerStatistics(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
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

    def __str__(self):
        return self.name
