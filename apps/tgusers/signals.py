from .models import StartMessage
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
import requests


@receiver(post_save, sender=StartMessage)
def send_request_on_update(sender, instance, created, **kwargs):
    if not created:  # Проверяем, что это обновление
        url = 'https://httpbin.org/post'  # Замените на нужный URL

        # Подготовка данных для отправки
        data = {
            'id': instance.id,
            'text': instance.text,
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
        }

        # Отправка POST-запроса
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Проверка на ошибки
            print("Запрос успешно отправлен!")  # Принт для подтверждения
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")


@receiver(post_migrate)
def create_default_start_message(sender, **kwargs):
    if sender.name == 'your_app_name':
        if not StartMessage.objects.exists():
            StartMessage.objects.create(start_message='Начальное сообщение по умолчанию', text='Текст по умолчанию')
