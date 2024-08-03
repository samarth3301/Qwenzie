import discord
from discord.ext import commands
from core.bot import Bot


class GlobalEvents(commands.Cog):
    def __init__(self, bot: Bot):
        super().__init__()

    @commands.Cog.listener('on_guild_join')
    async def guild_join_event(self, ctx: commands.Context):
        pass

async def setup(bot: Bot):
    await bot.add_cog(GlobalEvents(bot))