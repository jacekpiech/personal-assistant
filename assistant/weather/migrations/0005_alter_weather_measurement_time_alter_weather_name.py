# Generated by Django 5.0.6 on 2024-06-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_alter_weather_measurement_time_alter_weather_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='measurement_time',
            field=models.TextField(default='17:21'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='name',
            field=models.CharField(default='Odczyt z dnia 2024-06-27', max_length=200),
        ),
    ]
