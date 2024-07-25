from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="tg_nickname",
        ),
        migrations.AddField(
            model_name="user",
            name="tg_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]