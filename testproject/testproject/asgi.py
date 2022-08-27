from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter, get_default_application
from chtest.routing import websockets
from chtest.consumers import AsyncWSConsumer
from .settings import *
import os
import django

django.setup()

application = ProtocolTypeRouter({
    "websocket": websockets,
    "channel": ChannelNameRouter({
        "test-channel-1": AsyncWSConsumer.as_asgi()
    })
})
