from rest_framework import serializers
from .models import Message
from .models import Message

from main_app.tasks import send_email


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        exclude = []

    def create(self, validated_data):
        title = validated_data['title']
        body = validated_data['body']
        position = validated_data['position']
        to_email = validated_data['to_email']

        send_email(title,
                         body,
                         position,
                         to_email)

        mail = Message.objects.create(title=title,
                                      body=body,
                                      to_email=to_email,
                                      position=position)

        return mail
