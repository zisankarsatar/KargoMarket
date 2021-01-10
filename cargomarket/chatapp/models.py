from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Chat(models.Model):
    members = models.ManyToManyField(User, related_name="chats")
    update_time = models.DateTimeField(auto_now=True)


class Message(models.Model):
    class Meta:
        ordering = ['send_time']

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField("message", max_length=100)
    send_time = models.DateTimeField(auto_now_add=True)


# Client1 -> WS1 -> Server -> CH1 

# CH1 -> Server -> WS2 -> Client2
#        Server -> WS3 -> Client3
#        Server -> WS1 -> Client1
