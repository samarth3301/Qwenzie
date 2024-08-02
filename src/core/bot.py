import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.presences = False

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            intents=intents,
        )