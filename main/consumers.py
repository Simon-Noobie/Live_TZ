import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TimeZoneConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.timezone = self.scope['url_route']['kwargs']['timezone']
        self.group_name = f"timezone_{self.timezone}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        pass

    async def send_time(self, event):
        await self.send(text_data=json.dumps({
            'time': event['time'],
            'timezone': self.timezone
        }))

