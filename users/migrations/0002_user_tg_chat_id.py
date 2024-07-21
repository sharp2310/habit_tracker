from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                help_text="Идентификатор чата в Telegram, который будет использоваться для отправки уведомлений",
                max_length=50,
                null=True,
                verbose_name="ID чата в Telegram",
            ),
        ),
    ]