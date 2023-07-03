# Generated by Django 4.2.3 on 2023-07-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battlebit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverstatistics',
            name='active_players',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='max_players',
            field=models.IntegerField(default=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serverstatistics',
            name='server_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
