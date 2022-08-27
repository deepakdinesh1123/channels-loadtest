from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from . import consumers

websockets = URLRouter([path("ws/test/<int:id>", consumers.AsyncWSConsumer.as_asgi())])
