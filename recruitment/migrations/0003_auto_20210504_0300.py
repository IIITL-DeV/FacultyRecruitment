# Generated by Django 2.2.20 on 2021-05-03 21:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20210503_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 3, 21, 30, 31, 681824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='defence_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 3, 21, 30, 31, 684514, tzinfo=utc)),
        ),
    ]