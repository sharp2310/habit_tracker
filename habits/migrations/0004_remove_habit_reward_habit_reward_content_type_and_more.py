from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("habits", "0003_alter_reward_options_habit_reward"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="reward",
        ),
        migrations.AddField(
            model_name="habit",
            name="reward_content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="reward_object_id",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]