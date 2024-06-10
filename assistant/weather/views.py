from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Weather


def weather_list(request):

    weather_entries = Weather.objects.all()
    return render(
        request, "weather/post/weather_list.html", {"weather_entries": weather_entries}
    )


def weather_detail(request, pk):
    weather_entry = get_object_or_404(Weather, pk=pk)
    return render(
        request, "weather/post/weather_detail.html", {"weather_entry": weather_entry}
   )
