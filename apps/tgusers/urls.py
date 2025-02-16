from django.urls import path
from .views import StartMessageView

urlpatterns = [
    path('start-message/', StartMessageView.as_view(), name='start_message_list_api'),
]
