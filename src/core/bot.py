import os
import discord
import config
import jishaku
import logging

from discord.ext import commands
from typing import List, Callable, Coroutine
from utils.logger import logger
from prisma import Prisma

intents = discord.Intents.all()
intents.presences = False

startup : List[Callable[["Bot"], Coroutine]] = []

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            intents=intents,
            activity=discord.CustomActivity(name="discord.gg/techsolace"),
            status=discord.Status.idle,
            owner_ids=config.owner_ids
        )

    @property
    def config(self) -> config:
        return __import__('config')

    @startup.append
    async def load_cogs(self):
        for files in os.listdir('./src/cogs'):
            if files.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{files[:-3]}')
                except Exception as e:
                    logger.error(e)
        await self.load_extension('jishaku')

    @startup.append
    async def connect_db(self):
        try:
            self.db = Prisma()
            await self.db.connect()
            logger.info('Connected to database.')
        except Exception as e:
            logger.error(e)


    async def setup_hook(self):
        await self.tree.sync()
        for tasks in startup:
            self.loop.create_task(tasks(self))

    async def on_close(self):
        await self.db.disconnect()

    @staticmethod
    async def on_message_edit(before: discord.Message, after: discord.Message):
        if not before.author.bot and before.content != after.content:
            await bot.process_commands(after)

    async def on_ready(self):
        logger.info(f"Logged in as {self.user}")

bot = Bot()
