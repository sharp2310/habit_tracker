from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Reward(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=100, verbose_name="Название вознаграждения")
    description = models.TextField(verbose_name="Описание вознаграждения", **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Вознаграждение"
        verbose_name_plural = "Вознаграждения"


class Habit(models.Model):
    #  варианты периодичности привычки
    DAILY = "Раз в день"
    EVERY_TWO_DAYS = "Раз в два дня"
    EVERY_THREE_DAYS = "Раз в три дня"
    EVERY_FOUR_DAYS = "Раз в четыре дня"
    EVERY_FIVE_DAYS = "Раз в пять дней"
    EVERY_SIX_DAYS = "Раз в шесть дней"
    WEEKLY = "Раз в неделю"

    PERIOD_CHOICES = (
        (DAILY, "Раз в день"),
        (EVERY_TWO_DAYS, "Раз в два дня"),
        (EVERY_THREE_DAYS, "Раз в три дня"),
        (EVERY_FOUR_DAYS, "Раз в четыре дня"),
        (EVERY_FIVE_DAYS, "Раз в пять дней"),
        (EVERY_SIX_DAYS, "Раз в шесть дней"),
        (WEEKLY, "Раз в неделю"),
    )

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Владелец привычки"
    )

    reward = models.ForeignKey(
        Reward, on_delete=models.SET_NULL, verbose_name="Вознаграждение", **NULLABLE
    )

    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка"
    )

    activity = models.CharField(max_length=150, verbose_name="Описание привычки")
    place = models.CharField(max_length=200, verbose_name="Место", **NULLABLE)
    time = models.TimeField(verbose_name="Время выполнения привычки", **NULLABLE)
    periodicity = models.CharField(
        choices=PERIOD_CHOICES, default=DAILY, verbose_name="Периодичность"
    )
    duration = models.DurationField(
        default=None, verbose_name="Продолжительность выполнения (в сек)", **NULLABLE
    )
    is_public = models.BooleanField(
        default=False, verbose_name="Признак публичности", **NULLABLE
    )
    is_pleasant = models.BooleanField(
        verbose_name="Признак приятной привычки", **NULLABLE
    )

    last_action = models.DateTimeField(
        auto_now_add=True, verbose_name="последнее сообщение", **NULLABLE
    )

    def __str__(self):
        return f"{self.activity}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"