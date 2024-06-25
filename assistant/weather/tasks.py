from assistant.celery import app as celery_app
from weather.utils import save_weather_data, populate_weather_summary


@celery_app.task(bind=True)
def task_save_weather_data(self):
    save_weather_data()
    populate_weather_summary()