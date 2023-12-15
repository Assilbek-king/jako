# Generated by Django 4.0.4 on 2023-12-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_diagram_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('card_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='diagram',
            name='percent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
