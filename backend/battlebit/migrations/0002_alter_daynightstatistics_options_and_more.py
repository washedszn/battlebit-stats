# Generated by Django 4.2.3 on 2023-07-15 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battlebit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daynightstatistics',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='gamemodestatistics',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='mapsizestatistics',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='mapstatistics',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='regionstatistics',
            options={'ordering': ['-timestamp']},
        ),
    ]
