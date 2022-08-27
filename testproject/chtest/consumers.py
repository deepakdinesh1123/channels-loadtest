import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

class AsyncWSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.id = str(self.scope["url_route"]["kwargs"]["id"])
        self.group_name = f"group_{self.id}"
        await self.channel_layer.group_add(
            self.group_name,
            "test-channel-1",
        )
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.id, {"type": "echo", "message": message}
        )
    
    async def echo(self, event):
        message = event["message"]
        await self.channel_layer.send(
            "test-channel-1",
            {
                "type": "message",
                "message": message,
            }
        )
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, "test-channel-1")

