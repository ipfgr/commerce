# Generated by Django 3.1.5 on 2021-01-21 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210121_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 14, 42, 14, 974768, tzinfo=utc)),
        ),
    ]