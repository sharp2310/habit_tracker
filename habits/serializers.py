from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    RelatedOrRewardHabit,
    DurationHabit,
    RelatedAndIsPleasant,
    AbsenceHabit,
    FrequencyHabit,
)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Habit"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RelatedOrRewardHabit(
                value_1="relate_habit",
                value_2="reward"
            ),
            DurationHabit(
                value_1="duration"
            ),
            RelatedAndIsPleasant(
                value_1="relate_habit",
                value_2="is_pleasant"
            ),
            AbsenceHabit(
                value_1="is_pleasant",
                value_2="reward",
                value_3="relate_habit"
            ),
            FrequencyHabit(
                value_1="periodicity"
            ),
        ]