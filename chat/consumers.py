# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room
from pprint import pprint
from channels.db import database_sync_to_async

# 비동기적 채팅 서버
class ChatConsumer(AsyncWebsocketConsumer):
    # 연결 요청 받음
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_id

        # 채팅방 그룹 이름 추가
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        room_id = self.scope['url_route']['kwargs']['room_id']
        await self.delete_user_or_room(room_id)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    @database_sync_to_async
    def get_room(self, room_id):
        return Room.objects.get(pk=room_id)
    
    @database_sync_to_async
    def delete_user_or_room(self, room_id):
        room = Room.objects.get(pk=room_id)
        room.count_users -= 1
        room.save()
        if room.count_users <= 0:
            room.delete()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))