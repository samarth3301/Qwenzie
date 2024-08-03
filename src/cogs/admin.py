import config
import discord
from discord.ext import commands
from core.bot import Bot

class AdminCommands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @commands.group(
        name='panel'
    )
    @commands.has_permissions(administrator=True)
    async def panel(self, ctx: commands.Context):
        embed = discord.Embed(
            color=config.Color.default,
            description=
            f'> **`create` :** creates a panel.\n'
            f'> **`delete` :** removes a panel.\n'
            f'> **`show  ` :** view\'s panel configurations.'
        )
        embed.set_author(name='panel Commands')
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.reply(embed=embed, mention_author=False)
    
    @panel.command(
        name='create',
        aliases=['add']
    )
    @commands.has_permissions(administrator=True)
    async def panel_add(self, ctx: commands.Context):
        embed = discord.Embed(
            color=config.Color.default,
            description=''
        )

    @panel.command(
        name='delete',
        aliases=['remove']
    )
    @commands.has_permissions(administrator=True)
    async def panel_remove(self, ctx: commands.Context):
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
            f'> panels: {guildData.panel_count}'
        )
        embed.set_author(name=f'{ctx.guild.name}\'s config')
        await ctx.reply(embed=embed, view=None)
    
async def setup(bot: Bot):
    await bot.add_cog(AdminCommands(bot))