from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reward",
            options={"verbose_name": "Награда", "verbose_name_plural": "Награды"},
        ),
        migrations.AddField(
            model_name="habit",
            name="reward",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="habits.reward",
                verbose_name="Награда",
            ),
        ),
    ]