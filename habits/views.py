from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Reward, Habit
from habits.paginations import CustomPagination
from habits.serializers import RewardSerializer, HabitSerializer

from users.permissions import IsOwner


class RewardViewSet(viewsets.ModelViewSet):
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()

    def perform_create(self, serializer):
        """
        Метод получения владельца курса
        :param serializer: на вход получаем сериализатор
        """
        reward = serializer.save()
        reward.owner = self.request.user
        reward.save()


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """
        Метод получения владельца курса
        :param serializer: на вход получаем сериализатор
        """
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        elif user.is_authenticated:
            return Habit.objects.filter(owner=user)


class HabitIsPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self, *args, **kwargs):
        """
        Метод получения публичных уроков
        """
        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habit.objects.filter(owner=user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Habit.objects.filter(owner=user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )