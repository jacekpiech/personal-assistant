# Generated by Django 5.0.6 on 2024-06-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_weather_measurement_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='measurement_time',
            field=models.TextField(default='16:38'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='name',
            field=models.CharField(default='Odczyt z dnia 2024-06-18', max_length=200),
        ),
    ]
