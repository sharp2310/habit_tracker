from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="send_date",
            field=models.DateField(
                auto_now_add=True,
                null=True,
                verbose_name="дата начала отправки"
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="action",
            field=models.TextField(
                help_text="Опишите действие. Например, ходить в спортзал",
                max_length=300,
                verbose_name="Действие, которое следует выполнять",
            ),
        ),
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
                help_text="Укажите периодичность. Например, DAILY",
                verbose_name="Периодичность",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="place",
            field=models.CharField(
                help_text="Укажите место. Например, 'спортзал'",
                max_length=150,
                verbose_name="Место привычки",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(
                help_text="Укажите время по примеру: '18:00:00'",
                verbose_name="Время выполнения привычки",
            ),
        ),
    ]