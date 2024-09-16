from django.urls import path
from .views import UploadScreenshotView

urlpatterns = [
    path('upload-screenshot/<int:payment_id>/', UploadScreenshotView.as_view(), name='upload-screenshot'),
]
