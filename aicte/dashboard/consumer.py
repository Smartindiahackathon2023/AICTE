import json
from asgiref.sync import async_to_sync
from register.models import Developer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from django.contrib.auth.models import User

class PersonalChatConsumer(WebsocketConsumer):
    def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        reciever_id = data['reciever_id']
        sender_id=data['sender_id']
        reciever=Developer.objects.get(id=reciever_id)
        sender=Developer.objects.get(id=sender_id)
        self.save_message(sender, self.room_group_name, message)
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id,
                'reciever_id': reciever_id
            }
        )
    def chat_message(self, event):
        message = event['message']
        
        
        self.send(text_data=json.dumps({
            'message': message,
            'sender_id' : event['sender_id'],
            'reciever_id': event['reciever_id']
        }))
        print("msg sent")
    
    def save_message(self, sender, thread_name, message):
        print("Message going to saved")
        new_message = Message.objects.create(
            sender=sender, message=message, thread_name=thread_name)
        new_message.save()
        return "Succes"