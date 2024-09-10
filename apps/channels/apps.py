from django.apps import AppConfig


class ChannelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.channels'

    def ready(self):
        # Подключаем сигнал
        from . import signals  # Убедитесь, что файл signals существует и правильно импортирован
