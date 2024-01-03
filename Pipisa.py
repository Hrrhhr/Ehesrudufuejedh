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
    """Модуль для @pipisabot"""

    strings = {"name": "Piska"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('@MVPMihail', "/dick@pipisabot")
            await asyncio.sleep(1680)
            loop = asyncio.get_event_loop()
task = loop.create_task(test())
loop.run_until_complete(asyncio.sleep(3))
task.cancel()

    @loader.unrestricted
    @loader.ratelimit
    async def Dickcmd(self, message):
        """Ещё маленькая пипися."""
        if self.tasks:
            return await message.edit("Ты уже растишь пиписю.")
        await message.edit("Ты начал растить пиписю.")
        client = message.client
        self.tasks = [asyncio.create_task(self.b_run(client))] 
    @loader.unrestricted
    @loader.ratelimit
    async def BigDickcmd(self, message):
        """Уже большая пипися"""
        if not self.tasks:
            return await message.edit("Ты не растишь пиписю.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Ты прекратил растить пиписю.")

