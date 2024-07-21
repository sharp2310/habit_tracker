import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_tg


@shared_task
def send_habit():
    habits = Habit.objects.all()  # Получаем все привычки
    current_date = datetime.datetime.now()  # Текущее время
    for habit in habits:
        if habit.time == current_date:
            tg_chat = habit.user.tg_chat_id
            message = f"Я буду {habit.action} в {habit.time} в {habit.place}."
            send_tg(tg_chat, message)  # Отправляем привычку в Telegram чат