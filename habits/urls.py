from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitPublishListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    # habits
    path(
        "",
        HabitListAPIView.as_view(),
        name="habits_list"
    ),
    path(
        "published/",
        HabitPublishListAPIView.as_view(),
        name="habits_published"
    ),
    path(
        "create/",
        HabitCreateAPIView.as_view(),
        name="habits_create"
    ),
    path(
        "<int:pk>/",
        HabitRetrieveAPIView.as_view(),
        name="habits_retrieve"
    ),
    path(
        "update/<int:pk>/",
        HabitUpdateAPIView.as_view(),
        name="habits_update"
    ),
    path(
        "delete/<int:pk>",
        HabitDestroyAPIView.as_view(),
        name="habits_delete"
    ),
]