from rest_framework import serializers
from .models import ButtonMessage, StartMessage


class ButtonMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonMessage
        fields = ['id', 'type', 'name', 'url', 'callback_data']


class StartMessageSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo_url')
    video = serializers.SerializerMethodField('get_video_url')
    buttons = ButtonMessageSerializer(many=True)

    class Meta:
        model = StartMessage
        fields = ['id', 'text', 'photo', 'video', 'buttons']

    def get_photo_url(self, obj):
        if obj.photo:
            photo_url = 'https://bot.chertovich.me' + obj.photo.url
        else:
            photo_url = None
        return photo_url

    def get_video_url(self, obj):
        if obj.video:
            video_url = 'https://bot.chertovich.me' + obj.video.url
        else:
            video_url = None
        return video_url
