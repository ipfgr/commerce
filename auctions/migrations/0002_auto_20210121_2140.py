# Generated by Django 3.1.5 on 2021-01-21 14:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 14, 40, 12, 58350, tzinfo=utc)),
        ),
    ]