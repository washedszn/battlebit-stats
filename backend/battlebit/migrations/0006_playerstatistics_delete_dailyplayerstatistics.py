# Generated by Django 4.2.3 on 2023-07-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battlebit', '0005_dailyplayerstatistics_max_players_at_0_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStatistics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('region', models.CharField(max_length=30)),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='DailyPlayerStatistics',
        ),
    ]
