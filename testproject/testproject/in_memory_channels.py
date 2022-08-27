from .settings import *

INSTALLED_APPS.append("channels")

ASGI_APPLICATION = 'testproject.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
