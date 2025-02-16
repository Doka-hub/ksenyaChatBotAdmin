from django.apps import AppConfig


class TgusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tgusers'
    verbose_name = 'Телеграм Пользователи'

    def ready(self):
        from . import signals  # noqa
