from django.urls import path

from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import (
    RewardViewSet,
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView, HabitIsPublicListAPIView,
)

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"rewards", RewardViewSet, basename="reward")

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("public_list/", HabitIsPublicListAPIView.as_view(), name="habit_is_public"),
    path(
        "<int:pk>/",
        HabitRetrieveAPIView.as_view(),
        name="habit_retrieve",
    ),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
] + router.urls