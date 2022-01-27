from rest_framework.viewsets import ModelViewSet

from main_app.models import Message
from main_app.serializer import MessageSerializer


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
