from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_user_tg_nickname_user_tg_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]