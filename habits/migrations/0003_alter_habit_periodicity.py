from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0002_habit_send_date_alter_habit_action_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.CharField(
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
                help_text="Укажите периодичность. Например, Раз в день",
                verbose_name="Периодичность",
            ),
        ),
    ]