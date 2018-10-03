# Generated by Django 2.1.2 on 2018-10-03 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20181003_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 3, 43, 39, 690623)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 3, 43, 39, 690651)),
        ),
        migrations.AlterField(
            model_name='moviedetails',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 3, 43, 39, 691097)),
        ),
        migrations.AlterField(
            model_name='moviedetails',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 3, 43, 39, 691117)),
        ),
        migrations.AlterField(
            model_name='movieedithistory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 3, 43, 39, 691558)),
        ),
        migrations.AlterField(
            model_name='movieedithistory',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 3, 43, 39, 691576)),
        ),
    ]