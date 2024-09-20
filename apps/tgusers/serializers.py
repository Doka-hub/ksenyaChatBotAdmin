from rest_framework import serializers
from .models import StartMessage


class StartMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartMessage
        fields = ['id', 'start_message', 'text', 'created_at', 'updated_at']  # Укажите поля, которые хотите сериализовать
