from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from rest_framework.response import Response


def send_email(title, body, position, to_email):
    send_mail(
        subject=title,
        message=f"{position}\n{body}",
        from_email=None,
        recipient_list=[to_email]
    )
