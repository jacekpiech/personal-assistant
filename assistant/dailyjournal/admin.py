from django.contrib import admin
from .models import Journal


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ["title", "create_date", "mood_rate", "recovery_percentage_rating"]
    list_filter = ["title", "create_date", "mood_rate", "recovery_percentage_rating"]
    search_fields = ["title", "create_date", "update_date", "reflections", "good_things", "wake_up_time", "bed_time", "sleep_time", "number_of_steps", "running_distance", "bicycle_distance", "cold_shower", "activity_strength", "sleep_rate", "stress_rate", "mood_rate", "recovery_percentage_rating"]
    date_hierarchy = "create_date"
    ordering = ["create_date"]
    fields = ["title", "create_date", "update_date", "reflections", "good_things", "wake_up_time", "bed_time", "sleep_time", "number_of_steps", "running_distance", "bicycle_distance", "cold_shower", "activity_strength", "sleep_rate", "stress_rate", "mood_rate", "recovery_percentage_rating"]
    readonly_fields = ["create_date", "update_date"]