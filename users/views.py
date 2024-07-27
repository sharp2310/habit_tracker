from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer, UserProfileSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт для регистрации пользователя.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """
    Эндпоинт для получения списка пользователей.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # для тестов, не забыть удалить


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Эндпоинт для получения информации о пользователе.
    """

    serializer_class = UserSerializer

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.pk == self.kwargs["pk"]:
            return UserSerializer
        else:
            return UserProfileSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Эндпоинт для обновления информации о пользователе.
    """

    serializer_class = UserSerializer

    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Эндпоинт для удаления пользователя.
    """

    queryset = User.objects.all()