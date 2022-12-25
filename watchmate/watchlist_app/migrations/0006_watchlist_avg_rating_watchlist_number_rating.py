# Generated by Django 4.1.4 on 2022-12-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_rename_watchlist_review_watchlist_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]