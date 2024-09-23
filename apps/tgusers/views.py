from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import StartMessage
from .serializers import StartMessageSerializer


class SingleStartMessageView(RetrieveAPIView):
    serializer_class = StartMessageSerializer

    def get(self, request, *args, **kwargs):
        start_message = StartMessage.objects.first()

        if start_message is None:
            return Response({"detail": "No StartMessage found."}, status=404)

        serializer = self.get_serializer(start_message)
        return Response(serializer.data)
