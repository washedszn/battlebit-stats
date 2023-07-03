# Generated by Django 4.2.3 on 2023-07-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battlebit', '0002_serverstatistics_active_players_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverstatistics',
            name='active_players',
        ),
        migrations.RemoveField(
            model_name='serverstatistics',
            name='server_name',
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='anti_cheat',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='build',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='day_night',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='game_mode',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='has_password',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='hz',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='is_official',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='map',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='map_size',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='name',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='players',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='queue_players',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='region',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='serverstatistics',
            name='max_players',
            field=models.IntegerField(default=0),
        ),
    ]
