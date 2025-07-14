import pytz
from datetime import datetime
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from Live_TZ.celery import app

TIMEZONES = [
    'UTC',
    'America/New_York',
    'Europe/London',
    'Asia/Kolkata',
]

@app.task
def broadcast_time():
    channel_layer = get_channel_layer()
    for tz in TIMEZONES:
        now = datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S')
        group_name = f'timezone_{tz}'
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'send_time',
                'time': now,
            }
        )

