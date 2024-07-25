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
                    "place",
                    models.CharField(
                        max_length=150,
                        verbose_name="Место привычки"),
                ),
                ("time", models.TimeField(
                    verbose_name="Время выполнения привычки")
                 ),
                (
                    "action",
                    models.TextField(
                        max_length=300,
                        verbose_name="Действие, которое следует выполнять",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="Признак приятной привычки"
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
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Награда за выполнение",
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
                    "relate_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель привычки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]