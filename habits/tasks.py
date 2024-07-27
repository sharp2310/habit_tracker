from datetime import datetime, timedelta

from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_tg_reminder():
    """
    Функция проверки отправки сообщений
    с ориентированнием на последнее отправленное сообщение.
    """
    datetime_now = timezone.now()
    time_now = datetime.now()

    habits_list = Habit.objects.all()

    for habit in habits_list:
        last_action_date = habit.last_action or datetime_now - timedelta(
            days=999
        )  # Используем очень старую дату, если нет last_action_date
        send_message = False
        if habit.owner.is_active:
            if not habit.is_pleasant:
                if habit.periodicity == Habit.DAILY:
                    send_message = (datetime_now - last_action_date).days >= 1
                elif habit.periodicity == Habit.EVERY_TWO_DAYS:
                    send_message = (datetime_now - last_action_date).days >= 2
                elif habit.periodicity == Habit.EVERY_THREE_DAYS:
                    send_message = (datetime_now - last_action_date).days >= 3
                elif habit.periodicity == Habit.EVERY_FOUR_DAYS:
                    send_message = (datetime_now - last_action_date).days >= 4
                elif habit.periodicity == Habit.EVERY_FIVE_DAYS:
                    send_message = (datetime_now - last_action_date).days >= 5
                elif habit.periodicity == Habit.EVERY_SIX_DAYS:
                    send_message = (datetime_now - last_action_date).days >= 6
                elif habit.periodicity == Habit.WEEKLY:
                    send_message = (datetime_now - last_action_date).days >= 7

                if send_message:
                    if time_now.time() >= habit.time:
                        chat_id = habit.owner.chat_id
                        massage = f'Пора выполнить привычку "{habit.activity}"'

                        send_tg_message(chat_id, massage)

                        habit.last_try = datetime_now
                        habit.save()