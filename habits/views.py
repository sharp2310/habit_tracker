from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListAPIView(generics.ListAPIView):
    """Список всех привычек."""

    serializer_class = HabitSerializer

    def get_queryset(self):
        """Получаем привычки текущего пользователя"""

        user = self.request.user
        return Habit.objects.filter(user=user)

    pagination_class = HabitPagination


class HabitPublishListAPIView(generics.ListAPIView):
    """Список публичных привычек."""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPagination


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """Делаем текущего пользователя 'Создателем' привычки"""
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение одной привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Изменение привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]