# Generated by Django 5.0.6 on 2024-06-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_alter_weather_measurement_time_alter_weather_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='measurement_time',
            field=models.TextField(default='17:22'),
        ),
    ]
