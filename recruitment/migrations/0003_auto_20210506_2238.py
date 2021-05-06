# Generated by Django 2.2.20 on 2021-05-06 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20210505_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('email', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('google_login', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 6, 17, 8, 27, 616132, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='defence_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 6, 17, 8, 27, 625434, tzinfo=utc)),
        ),
    ]