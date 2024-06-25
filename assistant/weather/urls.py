from django.urls import path

from weather import views

app_name = "weather"
urlpatterns = [
    path("", views.weather_list, name="weather_list"),
    path("<int:pk>/", views.weather_detail, name="weather_detail"),
    path("test/", views.test_tailwind, name="test_tailwind"),
]
