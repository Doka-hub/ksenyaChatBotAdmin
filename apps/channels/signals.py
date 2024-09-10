from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Channel


@receiver(post_migrate)
def create_default_channel(sender, **kwargs):
    if sender.name == 'apps.channels':
        # Проверяем, если таблица уже создана, и если каналов нет, создаем новый
        if Channel.objects.count() == 0:
            Channel.objects.create(
                name='Channel 1',
                url='https://example.com',
                eur_amount='1000',
                rub_amount='1000',
            )
