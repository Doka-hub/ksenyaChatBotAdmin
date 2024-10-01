from rest_framework import serializers
from .models import StartMessage


class StartMessageSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo_url')
    video = serializers.SerializerMethodField('get_video_url')

    class Meta:
        model = StartMessage
        fields = ['id', 'text', 'photo', 'video']

    def get_photo_url(self, obj):
        if obj.photo:
            photo_url = 'http://localhost:8001' + obj.photo.url
        else:
            photo_url = None
        return photo_url

    def get_video_url(self, obj):
        if obj.video:
            video_url = 'http://localhost:8001' + obj.video.url
        else:
            video_url = None
        return video_url
