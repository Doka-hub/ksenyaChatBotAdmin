from django.apps import AppConfig


class TgusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tgusers'

    def ready(self):
        from . import signals
        from .models import StartMessage

        if not StartMessage.objects.exists():
            StartMessage.objects.create(text='Текст по умолчанию')
