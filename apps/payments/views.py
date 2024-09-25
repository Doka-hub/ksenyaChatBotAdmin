from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Payment
from .serializers import PaymentScreenshotSerializer


class UploadScreenshotView(APIView):
    def post(self, request):
        payment_id = request.data.get('payment_id')
        screenshot_file = request.FILES.get('screenshot')
        
        payment = get_object_or_404(Payment, id=payment_id)
        serializer = PaymentScreenshotSerializer(payment, data={'payment_screenshot': screenshot_file}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"Сообщение": "Скриншот успешно загружен"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
