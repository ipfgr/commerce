# Generated by Django 3.1.5 on 2021-01-22 13:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210122_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 13, 45, 32, 463145, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 13, 45, 32, 462146, tzinfo=utc)),
        ),
    ]
