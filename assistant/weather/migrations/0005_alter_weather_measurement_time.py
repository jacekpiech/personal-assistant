# Generated by Django 5.0.6 on 2024-05-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_alter_weather_measurement_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='measurement_time',
            field=models.TextField(default='18:39'),
        ),
    ]
