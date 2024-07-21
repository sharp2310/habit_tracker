import requests

from config.settings import BOT_TOKEN, TELEGRAM_URL


def send_tg(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", params=params)