from django.urls import re_path,path

from . import consumer

websocket_urlpatterns = [
    path('ws/<int:id>/', consumer.PersonalChatConsumer.as_asgi()),
]