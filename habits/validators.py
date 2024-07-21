from datetime import timedelta

from rest_framework.serializers import ValidationError


class RelatedOrRewardHabit:
    """
    Валидатор исключает одновременный выбор связанной привычки и вознаграждения
    """

    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def __call__(self, habit):
        if habit.get(self.value_1) and habit.get(self.value_2):
            raise ValidationError(
                "Нельзя выбрать одновременно связанную привычку и вознаграждение"
            )


class DurationHabit:
    """Валидация по продолжительности привычки не более 120 сек"""

    def __init__(self, value_1):
        self.value_1 = value_1

    def __call__(self, habit):
        if habit.get(self.value_1) is not None:
            if habit.get(self.value_1) > timedelta(seconds=120):
                raise ValidationError(
                    "Продолжительность привычки не может быть более 120 секунд"
                )


class RelatedAndIsPleasant:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def __call__(self, habit):
        if habit.get(self.value_1):
            if not habit.get(self.value_2):
                raise ValidationError(
                    "В связанной привычке должен быть признак приятной привычки"
                )


class AbsenceHabit:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __init__(self, value_1, value_2, value_3):
        self.value_1 = value_1
        self.value_2 = value_2
        self.value_3 = value_3

    def __call__(self, habit):
        if habit.get(self.value_1):
            if habit.get(self.value_2) or habit.get(self.value_3):
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                )


class FrequencyHabit:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней и не выполнять более 7 дней"""

    def __init__(self, value_1):
        self.value_1 = value_1

    def __call__(self, habit):
        if habit.get(self.value_1) < 1:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )
        elif habit.get(self.value_1) > 7:
            raise ValidationError("Нельзя выполнять привычку более 7 дней подряд.")