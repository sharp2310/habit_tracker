from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("habits", "0007_alter_habit_time_for_habit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="habits",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]