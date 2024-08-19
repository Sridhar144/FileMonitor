# monitor/consumers.py

import asyncio
import aiofiles
from channels.generic.websocket import AsyncWebsocketConsumer

class FileMonitorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.file_path = "/path/to/your/file"  # Replace with your file path
        self.file_handle = await aiofiles.open(self.file_path, mode='r')
        await self.file_handle.seek(0, 2)  # Move to the end of the file
        
        await self.accept()
        
        # Start a loop to send updates
        while True:
            # Read new lines asynchronously
            lines = await self.file_handle.readlines()
            if lines:
                await self.send(text_data=''.join(lines))
            await asyncio.sleep(1)  # Pause to prevent high CPU usage

    async def disconnect(self, close_code):
        await self.file_handle.close()

    async def receive(self, text_data):
        pass  # No need to handle incoming messages for this use case
