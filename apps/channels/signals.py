from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Channel


@receiver(post_migrate)
def create_default_channel(sender, **kwargs):
    if sender.name == 'apps.channels':
        if Channel.objects.count() == 0:
            Channel.objects.create(
                name='Channel 1',
                url='https://webhook.site/4cea51a6-bc98-4718-9ddf-648a2aa5b461',
                eur_amount='1000',
                rub_amount='1000',
            )
