from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from channels.auth import AuthMiddlewareStack
from main.consumers import TimeZoneConsumer

websocket_urlpatterns = [
    re_path(r'ws/time/(?P<timezone>[^/]+)/$', TimeZoneConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
