# Generated by Django 4.0.4 on 2023-12-16 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_userprofit_alter_userprofile_invest_sum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofit',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 16, 12, 52, 23, 204949)),
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 16, 12, 52, 23, 204949)),
        ),
    ]
