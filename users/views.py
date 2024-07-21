from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.paginations import UserPagination
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание нового пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (
        AllowAny,
    )  # Открывает доступ для неавторизованных пользователей

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Получение списка всех пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Получение информации о конкретном пользователе"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Изменение информации о пользователе"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление пользователя"""

    queryset = User.objects.all()