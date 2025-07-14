import json
from urllib.parse import unquote
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from datetime import datetime
import pytz

class TimeZoneConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_task = None

    async def connect(self):
        self.timezone = unquote(self.scope['url_route']['kwargs']['timezone'])
        self.group_name = f"timezone_{self.timezone.replace('/', '_')}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        self.time_task = asyncio.create_task(self.send_time_loop())

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        if self.time_task:
            self.time_task.cancel()

    async def receive(self, text_data):
        pass

    async def send_time(self, event):
        await self.send(text_data=json.dumps({
            'time': event['time'],
            'timezone': self.timezone
        }))

    async def send_time_loop(self):
        try:
            while True:
                tz = pytz.timezone(self.timezone)
                current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                await self.send(text_data=json.dumps({
                    'time': current_time,
                    'timezone': self.timezone
                }))
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
