from datetime import datetime

from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver

from .models import PaymentType, Payment
from .tasks import send_payment_request


@receiver(post_save, sender=Payment)
def payment_created(sender, instance, created, **kwargs):
    if not created:
        if instance.is_paid is True and instance.type == PaymentType.RB:
            send_payment_request.delay(instance.id)
            instance.paid_at = datetime.now ()
            instance.save()
