import openai
from django.conf import settings
from django.db.models import Q
from openai import OpenAI
from django.utils import timezone
from requests import get
from weather.models import Weather
import os


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
        data=response_data,

    )
    weather.save()


def save_weather_to_file(data: str, filepath: str = "weather.txt") -> None:
    with open(filepath, 'w') as f:
       f.write(data)


def prepare_data_transcript(weather:Weather) -> str:
    data = f"""Dane pogodowe dla stacji: {weather.data['stacja']}
    Odczyt w godzinie: {weather.measurement_time} w dniu: {weather.name}
    Temperatura: {weather.temperature}
    Opad: {weather.rainfall}
    Wilgotność: {weather.humidity}
    Wiatr: {weather.wind_speed}
    Ciśnienie: {weather.pressure}""".replace("\t","").replace("    ", "")
    print(data)
    return data

def read_data_weather_from_file(filepath: str = "weather.txt") -> str:
    with open(filepath, "r") as f:
        return f.read()


def get_weather_summary_GPT(transcript: str) -> str:
    """Pobierz i zwróć podsumowanie pogody z API GPT"""
    client = OpenAI(
        api_key=settings.GPT_API_KEY
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Jesteś ekspertem od pogody."},
            {"role": "user",
             "content": "Podsumuj pogodę biorąc pod uwagę pomiary z dnia dzisiejszego. Sprawdź czy pogoda nadaje się na podróż rowerem i spacerem"},
            {"role": "assistant", "content": "Yes."},
            {"role": "user", "content": transcript},
        ],
    )
    return str(response.choices[0].message.content)


def populate_weather_summary():
    weathers = Weather.objects.filter(Q(summary__isnull=True) | Q(summary=""))
    print("znalazłem", len(weathers))
    for weather in weathers:
        weather_parsed_data = prepare_data_transcript(weather)
        summary = get_weather_summary_GPT(weather_parsed_data)
        weather.summary = summary
        weather.save()





