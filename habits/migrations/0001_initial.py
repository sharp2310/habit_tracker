from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("action", models.CharField(max_length=255, verbose_name="Действие")),
                ("place", models.CharField(max_length=255, verbose_name="Место")),
                (
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Публичная"),
                ),
                (
                    "is_pleasent",
                    models.BooleanField(default=False, verbose_name="Полезная"),
                ),
                (
                    "frequency",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Количество повторений"
                    ),
                ),
                (
                    "time_to_complete",
                    models.DurationField(verbose_name="Время на выполнение"),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
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
                ("reward", models.CharField(max_length=255, verbose_name="Награда")),
            ],
        ),
    ]