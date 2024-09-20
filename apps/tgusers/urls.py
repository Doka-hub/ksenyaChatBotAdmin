from django.urls import path
from .views import StartMessageListView

urlpatterns = [
    path('start-message/', StartMessageListView.as_view(), name='start_message_list_api'),
]
