# FULLY FUNCTIONAL SYNC SERVER
# import json
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
        
#         # join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#         self.accept()

#     def disconnect(self, close_code):
#         # leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = str(text_data_json['message']).upper()

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']

#         # send message to web socket
#         self.send(text_data=json.dumps({'message': message}))


# ASYNC CHAT SERVER
import json 
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chatapp.models import Message, Chat
from datetime import datetime


class DBConnector:

    @staticmethod
    def save_message(message, chat_id, sender_user):
        chat = Chat.objects.get(id=chat_id)
        
        m = Message()
        m.chat = chat
        m.sender = sender_user
        m.message_text = message
        m.save()
        return m


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].id is None:
            self.close()

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = "chat_%s" % self.room_name

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        chat_id = text_data_json['chat_id']

        # Save message to DB, before send
        message_obj = await database_sync_to_async(DBConnector.save_message)(message, chat_id, self.scope["user"])
        dakika = message_obj.send_time.minute
        if dakika < 10:
            dakika = "0{}".format(dakika)
        send_time = "{}:{}".format(message_obj.send_time.hour, message_obj.send_time.minute)

        sender_id = self.scope["user"].id

        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'send_time': send_time,
                'sender': sender_id
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        send_time = event['send_time']

        await self.send(text_data=json.dumps(
            {'message': message, 'sender': event["sender"], 'send_time': send_time}
        ))