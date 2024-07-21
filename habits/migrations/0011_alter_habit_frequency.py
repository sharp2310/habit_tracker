from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0010_habit_last_remember"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="frequency",
            field=models.PositiveIntegerField(
                default=1, verbose_name="Количество повторений"
            ),
        ),
    ]