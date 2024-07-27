from rest_framework import serializers

from habits.models import Reward, Habit
from habits.validators import (
    HabitOrRewardValidator,
    ActivityDurationValidator,
    PleasantRelatedHabitValidator,
    NiceHabitValidator,
)


class RewardSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вознаграждения
    """

    class Meta:
        model = Reward
        fields = "__all__"


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для привычки
    """

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            HabitOrRewardValidator(field_1="related_habit", field_2="reward"),
            ActivityDurationValidator(field="duration"),
            PleasantRelatedHabitValidator(),
            NiceHabitValidator(
                field_1="is_pleasant", field_2="related_habit", field_3="reward"
            ),
        ]