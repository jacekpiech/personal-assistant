# Generated by Django 5.0.6 on 2024-05-27 17:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Odczyt z dnia 2024-05-27', max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('measurement_time', models.TextField(default='17:07')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('rainfall', models.FloatField(verbose_name='Opad deszczu')),
                ('summary', models.TextField()),
                ('air_quality', models.FloatField()),
                ('data', models.JSONField(default=dict)),
            ],
            options={
                'ordering': ['-date'],
                'indexes': [models.Index(fields=['date'], name='weather_wea_date_566e92_idx')],
            },
        ),
    ]
