from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="last_action",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="последнее сообщение"
            ),
        ),
    ]