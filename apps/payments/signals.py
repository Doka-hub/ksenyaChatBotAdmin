from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from .models import Payment, RBPaymentDetail
from .tasks import send_payment_request


@receiver(post_save, sender=Payment)
def payment_created(sender, instance, created, **kwargs):
    if instance.is_paid == True and instance.type == 'RB':
        send_payment_request.delay(instance.id)
