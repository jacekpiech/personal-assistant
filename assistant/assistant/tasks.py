from requests import get
from django.utils import timezone

from assistant.assistant.celery import app
from assistant.weather.models import Weather
from celery import shared_task


@shared_task
def save_weather_data():
    response = get(f'https://danepubliczne.imgw.pl/api/data/synop/station/lodz/')
    response_data: dict = response.json()

    weather = Weather(
        name=response_data['data_pomiaru'],
        date=timezone.now(),
        measurement_time=response_data['godzina_pomiaru'],
        temperature=response_data['temperatura'],
        humidity=response_data['wilgotnosc_wzgledna'],
        pressure=response_data['cisnienie'],
        wind_speed=response_data['predkosc_wiatru'],
        rainfall=response_data['suma_opadu'],
        air_quality=0,
        data=response_data
    )

    if Weather.objects.count() == 0 or Weather.objects.latest('date').measurement_time != weather.measurement_time:
        weather.save()


app.autodiscover_tasks()