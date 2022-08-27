from .settings import *
import os

INSTALLED_APPS += ["channels"]

ASGI_APPLICATION = 'testproject.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_rabbitmq.core.RabbitmqChannelLayer",
        'url': os.environ.get(
                'RABBITMQ_URL',
                'amqp://guest:guest@localhost:5672',
            ),
    },
}
