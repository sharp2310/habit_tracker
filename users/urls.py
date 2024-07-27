from django.urls import path

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    # users
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="delete"),
    # login/register
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]