from celery import shared_task
from config import settings
from main.models import Habit
import requests
from datetime import datetime

@shared_task
def send_message_to_bot():
    """ отправляет сообщение в телеграм-бот"""
    print("start")
    habits = Habit.objects.filter(is_good=False, time=datetime.utcnow())
    for habit in habits:
        requests.get(
            url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
            params={
                'chat_id': habit.user.chat_id,
                'text': f'Привет {habit.user}! Время выполнять {habit.action}. Место выполнения: {habit.place}.'
                        f'Это займет {habit.duration} минут!'
            }
        )


# @shared_task
# def send_message_to_bot():
#     """Отправляет сообщение в телеграм-бот"""
#     print("start")
#     habits = Habit.objects.filter(is_good=False, time=datetime.utcnow())
#     for habit in habits:
#         response = requests.post(
#             url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/getUpdates',
#         )
#         if response.ok:
#             print("Запрос выполнен успешно")
#             updates = response.json()['result']
#             for update in updates:
#                 chat_id = update['message']['chat']['id']
#                 message = f'Привет {habit.user}! Время выполнять {habit.action}. Место выполнения: {habit.place}. ' \
#                           f'Это займет {habit.duration} минут!'
#
#                 requests.get(
#                     url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
#                     params={
#                         'chat_id': chat_id,
#                         'text': message
#                     }
#                 )
#         else:
#             print("Ошибка при выполнении запроса:", response['description'])