# Generated by Django 3.1.5 on 2021-01-22 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210122_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 11, 40, 23, 379055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.CharField(default='unknow', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 11, 40, 23, 379055, tzinfo=utc)),
        ),
    ]
