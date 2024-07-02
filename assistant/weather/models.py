from django.db import models
from django.utils import timezone


# Create your models here.
class Weather(models.Model):
    name = models.CharField(max_length=200, default="Odczyt z dnia " + timezone.now().strftime("%Y-%m-%d"))
    date = models.DateTimeField(default=timezone.now)
    measurement_time = models.TextField(default=timezone.now().strftime("%H:%M")) #todo convert to datetime
    temperature = models.FloatField()
    """Temperatura w stopniach celsjusza"""

    humidity = models.FloatField()
    """Wilgotność powietrza w procentach"""

    pressure = models.FloatField()
    wind_speed = models.FloatField()
    rainfall = models.FloatField(verbose_name="Opad deszczu")
    summary = models.TextField(null=True,blank=True,verbose_name="Podsumowanie pogody OpenAI", help_text="Tekst zwrotny z chatGPT, domyślnie pusty")
    air_quality = models.FloatField()
    data = models.JSONField(default=dict)


    class Meta:
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["date"]),
        ]

    def __str__(self):
        return self.name
