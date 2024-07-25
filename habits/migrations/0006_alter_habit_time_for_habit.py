import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0005_habit_time_for_habit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time_for_habit",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="Время выполнения привычки"
            ),
        ),
    ]