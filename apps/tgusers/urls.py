from django.urls import path
from .views import SingleStartMessageView

urlpatterns = [
    path('start-message/', SingleStartMessageView.as_view(), name='start_message_list_api'),
]
