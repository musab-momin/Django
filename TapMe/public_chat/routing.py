from django.urls import re_path
from public_chat import consumers


websocket_urlpatterns = [
    re_path(r'ws/public-socket-server/', consumers.PublicChatConsumer.as_asgi())
]