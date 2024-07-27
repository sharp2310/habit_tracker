import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="Название вознаграждения"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание вознаграждения"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вознаграждение",
                "verbose_name_plural": "Вознаграждения",
            },
        ),
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "activity",
                    models.CharField(max_length=150, verbose_name="Описание привычки"),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Место"
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Время выполнения привычки"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("Раз в день", "Раз в день"),
                            ("Раз в два дня", "Раз в два дня"),
                            ("Раз в три дня", "Раз в три дня"),
                            ("Раз в четыре дня", "Раз в четыре дня"),
                            ("Раз в пять дней", "Раз в пять дней"),
                            ("Раз в шесть дней", "Раз в шесть дней"),
                            ("Раз в неделю", "Раз в неделю"),
                        ],
                        default="Раз в день",
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Продолжительность выполнения (в сек)",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        null=True,
                        verbose_name="Признак публичности",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец привычки",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "reward",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.reward",
                        verbose_name="Вознаграждение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]