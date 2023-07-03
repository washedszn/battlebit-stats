# Generated by Django 4.2.3 on 2023-07-03 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battlebit', '0007_serverstatistics_total_players'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamemodeaggstatistics',
            old_name='average_players',
            new_name='total_average_players',
        ),
        migrations.RenameField(
            model_name='mapaggstatistics',
            old_name='average_players',
            new_name='total_average_players',
        ),
        migrations.RenameField(
            model_name='regionaggstatistics',
            old_name='average_players',
            new_name='total_average_players',
        ),
        migrations.RenameField(
            model_name='serveraggstatistics',
            old_name='average_players',
            new_name='total_average_players',
        ),
        migrations.RenameField(
            model_name='timestatistics',
            old_name='average_players',
            new_name='total_average_players',
        ),
        migrations.RemoveField(
            model_name='gamemodeaggstatistics',
            name='max_players',
        ),
        migrations.RemoveField(
            model_name='gamemodeaggstatistics',
            name='min_players',
        ),
        migrations.RemoveField(
            model_name='mapaggstatistics',
            name='max_players',
        ),
        migrations.RemoveField(
            model_name='mapaggstatistics',
            name='min_players',
        ),
        migrations.RemoveField(
            model_name='regionaggstatistics',
            name='max_players',
        ),
        migrations.RemoveField(
            model_name='regionaggstatistics',
            name='min_players',
        ),
        migrations.RemoveField(
            model_name='serveraggstatistics',
            name='max_players',
        ),
        migrations.RemoveField(
            model_name='serveraggstatistics',
            name='min_players',
        ),
        migrations.RemoveField(
            model_name='timestatistics',
            name='max_players',
        ),
        migrations.RemoveField(
            model_name='timestatistics',
            name='min_players',
        ),
    ]
