from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_remove_habit_reward_habit_reward_content_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="time_for_habit",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Время выполнения привычки"
            ),
        ),
    ]