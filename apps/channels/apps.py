from django.apps import AppConfig


class ChannelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.channels'
    verbose_name = 'Телеграм Каналы'

    def ready(self):
        from .models import Channel

        if Channel.objects.count() == 0:
            Channel.objects.create(
                name='Channel 1',
                url='https://webhook.site/4cea51a6-bc98-4718-9ddf-648a2aa5b461',
                eur_amount='1000',
                rub_amount='1000',
                duration=30,
            )
