from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0009_alter_habit_frequency"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="last_remember",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Последнее воспоминание"
            ),
        ),
    ]