from django.urls import path
from .views import UploadScreenshotView

urlpatterns = [
    path('<int:pk>/upload-screenshot/', UploadScreenshotView.as_view(), name='upload-screenshot'),
]
