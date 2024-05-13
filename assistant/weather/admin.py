from django.contrib import admin
from .models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ["date", "temperature", "humidity", "pressure", "wind_speed", "rainfall", "summary", "air_quality"]
    list_filter = ["date", "temperature", "humidity", "pressure", "wind_speed", "rainfall", "summary", "air_quality"]
    search_fields = ["date", "temperature", "humidity", "pressure", "wind_speed", "rainfall", "summary", "air_quality"]
    date_hierarchy = "date"
    ordering = ["date"]
    fields = ["date", "temperature", "humidity", "pressure", "wind_speed", "rainfall", "summary", "air_quality", "data"]
    readonly_fields = ["data"]
