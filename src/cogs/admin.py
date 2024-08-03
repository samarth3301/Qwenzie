import config
import discord
from discord.ext import commands
from core.bot import Bot

class AdminCommands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @commands.group(
        name='pannel'
    )
    @commands.has_permissions(administrator=True)
    async def pannel(self, ctx: commands.Context):
        embed = discord.Embed(
            color=config.Color.default,
            description='hello world'
        )
        await ctx.reply(embed=embed, mention_author=False)
    
    @pannel.command(
        name='create',
        aliases=['add']
    )
    @commands.has_permissions(administrator=True)
    async def pannel_add(self, ctx: commands.Context):
        pass

    @pannel.command(
        name='delete',
        aliases=['remove']
    )
    @commands.has_permissions(administrator=True)
    async def pannel_remove(self, ctx: commands.Context):
        pass


    @commands.group(
        name='config'
    )
    async def guild_configurations(self, ctx: commands.Context):
        guildData = await self.bot.db.guildconfig.find_first(
            where={
                'guildId' : ctx.guild.id
            }
        )
        embed = discord.Embed(
            color=config.Color.default,
            description=
            f'> prefix : {guildData.prefix}\n'
            f'> pannels: {guildData.pannel_count}'
        )
        embed.set_author(name=f'{ctx.guild.name}\'s config')
        await ctx.reply(embed=embed, view=None)
    
async def setup(bot: Bot):
    await bot.add_cog(AdminCommands(bot))