# Generated by Django 4.0.4 on 2023-12-15 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_userprofile_alter_diagram_percent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='invest_sum',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
