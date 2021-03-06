# Generated by Django 3.1.5 on 2021-01-22 14:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210122_2045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WatchList',
        ),
        migrations.AddField(
            model_name='product',
            name='winner',
            field=models.CharField(default='Not yet have Winner', max_length=100),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 14, 40, 37, 250412, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 14, 40, 37, 250412, tzinfo=utc)),
        ),
    ]
