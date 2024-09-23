from django.urls import path
from .views import UploadScreenshotView

urlpatterns = [
    path('upload-screenshot/', UploadScreenshotView.as_view(), name='upload-screenshot'),
]
