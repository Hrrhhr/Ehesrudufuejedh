# meta developer: @modwini
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class FarmPipisaBot(loader.Module):
    """Модуль для автоматического фарминга в пиписьки в боте @pipisabot"""

    strings = {"name": "pipisa"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('@pipisabot', "/dick@pipisabot")
            await asyncio.sleep(1200)

    @loader.unrestricted
    @loader.ratelimit
    async def farmcmd(self, message):
        """Запустить автоматический фарминг в боте"""
        if self.tasks:
            return true
    @loader.unrestricted
    @loader.ratelimit
    async def stopcmd(self, message):
        """Остановить автоматический фарминг в боте"""
        if not self.tasks:
            return await message.edit("Автоматический фарминг не запущен.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Автоматический фарминг остановлен.")
