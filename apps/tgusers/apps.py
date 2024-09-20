from django.apps import AppConfig


class TgusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tgusers'

    def ready(self):
        import apps.tgusers.signals
