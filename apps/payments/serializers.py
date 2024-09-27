from rest_framework import serializers

from .models import Payment


class PaymentScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['screenshot']
