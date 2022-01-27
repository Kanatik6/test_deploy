from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_email = models.EmailField()
    position = models.CharField(max_length=255)
    sended_at = models.DateTimeField(auto_now_add=True)
    looked = models.BooleanField(default=False)