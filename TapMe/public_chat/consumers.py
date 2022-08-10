import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class PublicChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'public'
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'you are connected to public chat room!' 
        }))
        
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(f'''User send this message {message}''')

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        
    def chat_message(self, event):
        message  = event['message']
        
        self.send(text_data=json.dumps({
            'type': 'public_chat',
            'message': message
        }))