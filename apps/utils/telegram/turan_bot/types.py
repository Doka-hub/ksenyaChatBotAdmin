from enum import Enum
from typing import TypeVar

user_id = TypeVar('user_id', bound=str)
tg_user_id = TypeVar('tg_user_id', bound=str)


class MessageType(Enum):
    DEFAULT = 'default'
    PRICE_LIST = 'price_list'
    ORDER = 'order'
    ACTIVATION = 'activation'
    DEACTIVATION = 'deactivation'
