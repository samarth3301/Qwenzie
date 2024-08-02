import config
import discord
from discord.ext import commands
from core.bot import Bot

class AdminCommands(commands.Cog):
    def __init__(self, bot: Bot):
        super().__init__()
    
    @commands.group(
        name='pannel'
    )
    async def pannel(self, ctx: commands.Context):
        embed = discord.Embed(
            color=config.Color.default,
            description='hello world'
        )
        await ctx.reply(embed=embed, mention_author=False)
    
    @pannel.command(
        name='add'
    )
    async def pannel_add(self, ctx: commands.Context):
        pass

    @pannel.command(
        name='remove'
    )
    async def pannel_remove(self, ctx: commands.Context):
        pass

async def setup(bot: Bot):
    await bot.add_cog(AdminCommands(bot))