from django.urls import path
from .views import StartMessageView

urlpatterns = [
    path('messages/', StartMessageView.as_view(), name='start_message_list_api'),
]
