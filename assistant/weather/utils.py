import openai
from openai import OpenAI
from django.utils import timezone
from requests import get
from weather.models import Weather
from dotenv import load_dotenv
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

    with open('weather.txt', 'w') as f:
        f.write('Dane pogodowe dla stacji: ' + response.json()['stacja'] + '\n')
        f.write('Odczyt w godzinie: ' + response.json()['godzina_pomiaru'] + ', w dniu: ' + response.json()[
            'data_pomiaru'] + '\n')
        f.write('Temperatura: ' + response.json()['temperatura'] + '\n')
        f.write('Opady: ' + response.json()['suma_opadu'] + '\n')
        f.write('Wilgotność: ' + response.json()['wilgotnosc_wzgledna'] + '\n')
        f.write('Wiatr: ' + response.json()['predkosc_wiatru'] + 'm/s' + '\n')
        f.write('Cisnienie: ' + response.json()['cisnienie'] + '\n')

    load_dotenv()
    api_key = os.getenv('API_KEY')

    client = OpenAI(
        api_key=api_key
    )

    with open("weather.txt", "r") as f:
        transcript = f.read()

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



    if Weather.objects.count() == 0 or Weather.objects.latest('date').measurement_time != weather.measurement_time:
        weather.summary = response.choices[0].message.content
        weather.save()