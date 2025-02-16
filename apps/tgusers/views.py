from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import StartMessage
from .serializers import StartMessageSerializer


class StartMessageView(RetrieveAPIView):
    serializer_class = StartMessageSerializer
    queryset = StartMessage.objects.all()

    def get(self, request, *args, **kwargs):
        message_type = request.query_params.get('type')
        match message_type:
            case 'greeter':
                start_message = StartMessage.objects.filter(type='GREETER').first()
            case 'after_subscribe':
                start_message = StartMessage.objects.filter(type='AFTER_SUBSCRIBE').first()
            case _:
                start_message = StartMessage.objects.first()

        if start_message is None:
            return Response({"detail": "No StartMessage found."}, status=404)

        serializer = self.get_serializer(start_message)
        return Response(serializer.data)
