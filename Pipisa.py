# meta developer: @MVPMihail
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class Farmpipisaabot(loader.Module):
    """Модуль для автоматического фарминга в игровом боте @pipisabot"""

    strings = {"name": "Piska"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('@gfxprimechat', "/dick@pipisabot")
            await client.send_message('@owlneverdiegroup', "/dick@pipisabot")
            await asyncio.sleep(43200)

    @loader.unrestricted
    @loader.ratelimit
    async def Pipisacmd(self, message):
        """Запустить автоматический фарминг в боте"""
        if self.tasks:
            return await message.edit("Автоматический фарминг уже запущен.")
        await message.edit("Автоматический фарминг запущен.")
        client = message.client
        self.tasks = [asyncio.create_task(self.b_run(client))] 
    @loader.unrestricted
    @loader.ratelimit
    async def offPipisacmd(self, message):
        """Остановить автоматический фарминг в боте"""
        if not self.tasks:
            return await message.edit("Автоматический фарминг не запущен.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Автоматический фарминг остановлен.")

