from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей.
    """

    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей.
    """

    class Meta:
        model = User
        exclude = (
            "password",
            "last_name",
            "chat_id",
            "is_staff",
            "is_superuser",
        )