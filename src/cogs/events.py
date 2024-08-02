import discord
from discord.ext import commands
from core.bot import Bot


class GlobalEvents(commands.Cog):
    def __init__(self, bot: Bot):
        super().__init__()