from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0006_alter_habit_time_for_habit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time_for_habit",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Время выполнения привычки",
            ),
        ),
    ]