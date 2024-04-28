import asyncio
import time

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySynceConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("websocket MySynceConsumer connected ...---***---...", event)
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        print("websocket receive ...---***---...", event)
        # self.send({"type": "websocket.send", "text": str(event)})
        delay = 0.01
        for word in range(100):
            self.send({"type": "websocket.send", "text": str(word)})
            time.sleep(delay)

    def websocket_disconnect(self, event):
        print("websocket disconnect ...---***---...", event)
        raise StopConsumer


class MyAsynceConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket MyAsynceConsumer connected ...---***---...", event)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print("websocket receive ...---***---...", event)

        # self.send({"type": "websocket.send", "text": str(event)})
        data = event["text"]
        words = data.split()
        delay = 0.01
        for word in range(100):
            await self.send({"type": "websocket.send", "text": str(word)})
            await asyncio.sleep(delay)

    async def websocket_disconnect(self, event):
        print("websocket disconnect ...---***---...", event)
        raise StopConsumer
