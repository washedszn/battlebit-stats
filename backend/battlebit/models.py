from django.db import models

class ServerStatistics(models.Model):
    server_name = models.CharField(max_length=200)
    active_players = models.IntegerField()
    max_players = models.IntegerField()
    
    def __str__(self):
        return self.server_name