# Generated by Django 3.1.5 on 2021-01-23 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20210122_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 15, 13, 22, 393706, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 15, 13, 22, 393706, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='imgurl',
            field=models.URLField(default='https://www.commonequity.com.au/wp-content/plugins/download-manager/assets/images/img-404.png'),
        ),
        migrations.AlterField(
            model_name='watchlistforuser',
            name='watchlist',
            field=models.CharField(default='None', max_length=100, unique=True),
        ),
    ]