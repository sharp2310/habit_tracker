import os
import requests

from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_URL


def send_tg_message(chat_id, message):
    """
    Отправляет сообщение в Телеграм чат с указанным chat_id
    """

    url = f"{TELEGRAM_URL}{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }

    # Отправьте запрос и получите ответ
    response = requests.post(url, params=params)

    # Проверьте статус ответа
    if response.status_code == 200:
        print("Сообщение отправлено")
    else:
        print(f"Ошибка {response.status_code}")