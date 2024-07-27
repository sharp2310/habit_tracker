from django.contrib import admin

from habits.models import Habit, Reward


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "reward",
        "related_habit",
        "activity",
        "place",
        "time",
        "periodicity",
        "duration",
        "is_public",
        "is_pleasant",
    )


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "title",
        "description",
    )