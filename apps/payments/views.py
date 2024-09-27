from rest_framework.generics import UpdateAPIView

from .models import Payment
from .serializers import PaymentScreenshotSerializer


class UploadScreenshotView(UpdateAPIView):
    serializer_class = PaymentScreenshotSerializer
    queryset = Payment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
