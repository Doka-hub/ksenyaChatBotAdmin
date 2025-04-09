import requests

from django.conf import settings

from .types import MessageType, user_id, tg_user_id


class TuranBotAPI:
    def __init__(self, url: str = settings.NOTIFY_URL):
        self.url = url

    def send_message(
        self,
        type_: MessageType = MessageType.DEFAULT,
        text: str = '',
        users_ids: list[tuple[user_id, tg_user_id]] | None = None,
        notification_id: int | None = None,
        image: str | None = None,
    ):
        if isinstance(type_, MessageType):
            type_ = type_.value

        data = {
            'type': type_,
            'message': text,
            'users_ids': users_ids,
            'notification_id': notification_id,
            'image': image,
        }
        response = requests.post(self.url, json=data)
        return response
