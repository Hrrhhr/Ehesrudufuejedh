import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class FarmMonacoMod(loader.Module):
    """Модуль для автоматического фарминга в игровом боте @MonacoGamebot"""

    strings = {"name": "MonacoFarm"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('@monacogamebot', "Ежедневный бонус")
            await asyncio.sleep(1200)

    async def p_run(self, client):
        while True:
            await client.send_message('@monacogamebot', "Бизнес снять")
            await asyncio.sleep(1920)

    async def l_run(self, client):
        while True:
            await client.send_message('@monacogamebot', "Город снять")
            await asyncio.sleep(1220)

    async def t_run(self, client):
        while True:
            await client.send_message('@monacogamebot', "Работать")
            await asyncio.sleep(1440)

    async def a_run(self, client):
        while True:
            await client.send_message('@monacogamebot', "Ферма снять")
            await asyncio.sleep(1680)
