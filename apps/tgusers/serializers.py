from rest_framework import serializers
from .models import StartMessage


class StartMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartMessage
        fields = ['id', 'text', 'created_at', 'updated_at']
