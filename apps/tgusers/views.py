from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StartMessage
from .serializers import StartMessageSerializer


class StartMessageListView(APIView):
    def get(self, request):
        messages = StartMessage.objects.all()
        serializer = StartMessageSerializer(messages, many=True)
        return Response(serializer.data)
