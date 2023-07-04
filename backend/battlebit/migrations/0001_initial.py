# Generated by Django 4.2.3 on 2023-07-04 11:22

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModeAggStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('period', models.CharField(choices=[('last_hour', 'Last Hour'), ('last_day', 'Last Day'), ('last_7_days', 'Last 7 Days')], default='last_day', max_length=20)),
                ('game_mode_name', models.CharField(default='N/A', max_length=50)),
                ('total_average_players', models.FloatField(default=0.0)),
                ('most_used_map', models.CharField(default='N/A', max_length=50)),
                ('most_used_region', models.CharField(default='N/A', max_length=100)),
                ('most_used_server', models.CharField(default='N/A', max_length=100)),
            ],
            options={
                'verbose_name': 'Game Mode Aggregate Statistic',
                'verbose_name_plural': 'Game Mode Aggregate Statistics',
            },
        ),
        migrations.CreateModel(
            name='MapAggStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('period', models.CharField(choices=[('last_hour', 'Last Hour'), ('last_day', 'Last Day'), ('last_7_days', 'Last 7 Days')], default='last_day', max_length=20)),
                ('map_name', models.CharField(default='N/A', max_length=50)),
                ('total_average_players', models.FloatField(default=0.0)),
                ('most_used_game_mode', models.CharField(default='N/A', max_length=50)),
                ('most_used_region', models.CharField(default='N/A', max_length=100)),
                ('most_used_server', models.CharField(default='N/A', max_length=100)),
            ],
            options={
                'verbose_name': 'Map Aggregate Statistic',
                'verbose_name_plural': 'Map Aggregate Statistics',
            },
        ),
        migrations.CreateModel(
            name='RegionAggStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('period', models.CharField(choices=[('last_hour', 'Last Hour'), ('last_day', 'Last Day'), ('last_7_days', 'Last 7 Days')], default='last_day', max_length=20)),
                ('region_name', models.CharField(default='N/A', max_length=100)),
                ('total_average_players', models.FloatField(default=0.0)),
                ('most_used_map', models.CharField(default='N/A', max_length=50)),
                ('most_used_game_mode', models.CharField(default='N/A', max_length=50)),
                ('most_used_server', models.CharField(default='N/A', max_length=100)),
            ],
            options={
                'verbose_name': 'Region Aggregate Statistic',
                'verbose_name_plural': 'Region Aggregate Statistics',
            },
        ),
        migrations.CreateModel(
            name='ServerAggStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('period', models.CharField(choices=[('last_hour', 'Last Hour'), ('last_day', 'Last Day'), ('last_7_days', 'Last 7 Days')], default='last_day', max_length=20)),
                ('server_name', models.CharField(default='N/A', max_length=100)),
                ('total_average_players', models.FloatField(default=0.0)),
                ('most_used_map', models.CharField(default='N/A', max_length=50)),
                ('most_used_game_mode', models.CharField(default='N/A', max_length=50)),
                ('most_used_region', models.CharField(default='N/A', max_length=100)),
                ('is_official', models.BooleanField(default=False)),
                ('has_password', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Server Aggregate Statistic',
                'verbose_name_plural': 'Server Aggregate Statistics',
            },
        ),
        migrations.CreateModel(
            name='TimeStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('period', models.CharField(choices=[('last_hour', 'Last Hour'), ('last_day', 'Last Day'), ('last_7_days', 'Last 7 Days')], default='last_day', max_length=20)),
                ('total_average_players', models.FloatField(default=0.0)),
                ('most_used_map', models.CharField(default='N/A', max_length=50)),
                ('most_used_game_mode', models.CharField(default='N/A', max_length=50)),
                ('most_used_region', models.CharField(default='N/A', max_length=100)),
            ],
            options={
                'verbose_name': 'Time Statistic',
                'verbose_name_plural': 'Time Statistics',
                'ordering': ['-timestamp'],
                'indexes': [models.Index(fields=['timestamp'], name='timestamp_idx')],
            },
        ),
        migrations.CreateModel(
            name='ServerStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('batch_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(default='N/A', max_length=100)),
                ('map', models.CharField(default='N/A', max_length=50)),
                ('map_size', models.CharField(default='N/A', max_length=50)),
                ('game_mode', models.CharField(default='N/A', max_length=50)),
                ('region', models.CharField(default='N/A', max_length=100)),
                ('players', models.IntegerField(default=0)),
                ('queue_players', models.IntegerField(default=0)),
                ('max_players', models.IntegerField(default=0)),
                ('hz', models.IntegerField(default=0)),
                ('day_night', models.CharField(default='N/A', max_length=50)),
                ('is_official', models.BooleanField(default=False)),
                ('has_password', models.BooleanField(default=False)),
                ('anti_cheat', models.CharField(default='N/A', max_length=50)),
                ('build', models.CharField(default='N/A', max_length=50)),
            ],
            options={
                'verbose_name': 'Server Statistic',
                'verbose_name_plural': 'Server Statistics',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['name', 'created_at', 'batch_id'], name='name_date_batch_idx')],
            },
        ),
    ]
