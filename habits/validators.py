from datetime import timedelta

from rest_framework.serializers import ValidationError


class HabitOrRewardValidator:
    """
    Проверка, что не выбрана одна из двух возможных привычек
    """

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        if value.get(self.field_1) and value.get(self.field_2):
            message = f"Невозможно выбрать сразу приятную привычку и вознаграждение"
            raise ValidationError(message)


class ActivityDurationValidator:
    """
    Проверка длительности привычки не более 120 секунд и не меньше 0
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field) is not None:
            if value.get(self.field) < timedelta(seconds=0):
                message = f"Продолжительность привычки не может быть меньше 0 секунд"
                raise ValidationError(message)
            elif value.get(self.field) > timedelta(seconds=120):
                message = f"Продолжительность привычки не может превышать 120 секунд"
                raise ValidationError(message)


class PleasantRelatedHabitValidator:
    """
    Проверка, что связанная привычка является приятной
    """

    def __call__(self, habit: dict):
        if related_habit := habit.get("related_habit"):
            if not related_habit.is_pleasant:
                message = f"Привычка не может быть связанной с вознаграждением"
                raise ValidationError(message)


class NiceHabitValidator:
    """
    Проверка, что у приятной привычки нет вознаграждения и связанной привычки
    """

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        if (
            value.get(self.field_1)
            and value.get(self.field_2)
            or value.get(self.field_1)
            and value.get(self.field_3)
        ):
            raise ValidationError(
                "У приятной привычки не может быть ни вознаграждения, ни связанной привычки"
            )