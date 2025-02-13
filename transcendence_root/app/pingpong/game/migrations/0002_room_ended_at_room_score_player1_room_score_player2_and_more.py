# Generated by Django 5.1.3 on 2024-12-31 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='ended_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='score_player1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='score_player2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='winner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
