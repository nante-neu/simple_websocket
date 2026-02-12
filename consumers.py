import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.camera_id = self.scope['url_route']['kwargs']['camera_id']
        self.room_name = 'parking_lobby' # Simple shared room
        
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        print(f"--- Connection started for: {self.camera_id} ---")

    async def receive(self, text_data):
        data = json.loads(text_data)
        rpi_id = data.get('device_id')
        msg = data.get('message')

        # 1. Print in your Terminal
        print(f"TERMINAL RECEIVED -> ID: {rpi_id} | MSG: {msg}")

        # 2. Send to the Template
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'broadcast_to_browser',
                'id_from_pi': rpi_id,
                'msg_from_pi': msg
            }
        )

    async def broadcast_to_browser(self, event):
        # This sends it to the JavaScript console and HTML
        await self.send(text_data=json.dumps({
            'device_id': event['id_from_pi'],
            'message': event['msg_from_pi']
        }))
