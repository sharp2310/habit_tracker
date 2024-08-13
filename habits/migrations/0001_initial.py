from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место выполнения привычки')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время выполнения привычки')),
                ('action', models.CharField(max_length=150, verbose_name='Действие привычки')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Флаг принятой привычки')),
                ('award', models.CharField(blank=True, max_length=150, null=True, verbose_name='Вознаграждение за выполнение привычки')),
                ('frequency', models.PositiveIntegerField(default=1, verbose_name='Периодичность привычки в днях')),
                ('duration', models.PositiveIntegerField(default=120, verbose_name='Время на выполнения привычки')),
                ('is_public', models.BooleanField(default=False, verbose_name='Флаг публикации')),
                ('link_pleasant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]