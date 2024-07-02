from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from tinymce.models import HTMLField


class Journal(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    reflections = HTMLField()
    good_things = HTMLField()
    wake_up_time = models.TimeField()
    bed_time = models.TimeField()
    sleep_time = models.FloatField()
    number_of_steps = models.IntegerField()
    running_distance = models.FloatField()
    bicycle_distance = models.FloatField()
    cold_shower = models.BooleanField()
    activity_strength = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    sleep_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    stress_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    mood_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    recovery_percentage_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
