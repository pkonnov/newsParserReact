import asyncio

from channels.consumer import AsyncConsumer


class GetNewsConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print('connect', event)
        await self.send({
            'type': 'websocket.accept',
            'text': 'text'
        })
        await asyncio.sleep(5)
        await self.send({
            'type': 'websocket.close',
        })

    async def websocket_disconnect(self,event):
        await self.send({
            'type': 'websocket.disconnect'
        })
