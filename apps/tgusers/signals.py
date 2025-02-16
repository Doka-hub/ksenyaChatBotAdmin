import requests
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver

from .models import StartMessage


@receiver(post_save, sender=StartMessage)
def send_request_on_update(sender, instance: StartMessage, created, **kwargs):
    if not created:  # Проверяем, что это обновление
        url = 'http://backend:8000/api/utils/messages'  # Замените на нужный URL

        # Подготовка данных для отправки
        data = {
            'id': instance.id,
            'type': 'start_message' if instance.type == 'GREETER' else 'after_subscribe' if instance.type == 'AFTER_SUBSCRIBE' else 'unknown',
            'text': instance.text,
            'photo': instance.get_photo_url(),
            'video': instance.get_video_url(),
        }

        # Отправка POST-запроса
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Проверка на ошибки
            print("Запрос успешно отправлен!")  # Принт для подтверждения
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
