# Generated by Django 4.1.5 on 2023-07-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0006_watchlist_avg_rating_watchlist_number_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='streamplatform',
            name='website',
            field=models.URLField(max_length=100, unique=True),
        ),
    ]
