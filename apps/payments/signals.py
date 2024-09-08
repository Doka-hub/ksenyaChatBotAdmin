from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment
from .tasks import send_payment_request


@receiver(post_save, sender=Payment)
def payment_created(sender, instance, created, **kwargs):
    if created:
        send_payment_request.delay(instance.id)
