# Generated by Django 4.2.3 on 2023-07-03 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('battlebit', '0003_remove_serverstatistics_active_players_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverstatistics',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
