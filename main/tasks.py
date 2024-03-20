from celery import shared_task
from config import settings
from main.models import Habit
import requests
from datetime import datetime

@shared_task
def send_message_to_bot():
    """ отправля)ет сообщение в телеграм-бот"""
    print ("start")
    habits = Habit.objects.filter(is_good=False, time=datetime.utcnow())
    for habit in habits:
        requests.get(
            url=f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
            params={
                'chat_id': habit.user.telegram_id,
                'text': f'Привет {habit.user}! Время выполнять {habit.action}. Место выполнения: {habit.place}.'
                        f'Это займет {habit.duration} минут!'
            }
        )