from .settings import *
import os

INSTALLED_APPS += ["channels", "channels_redis" ]

ASGI_APPLICATION = 'testproject.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379')],
        },
    },
}
