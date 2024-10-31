import config
import discord
from discord.ext import commands
from core.bot import Bot
from tools.view.admin_pannel import CreatePannelView

class AdminCog(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.group(
        name='panel',
    )
    @commands.has_permissions(administrator=True)
    async def panel(self, ctx: commands.Context):
        embed = discord.Embed(
            color=config.Color.default,
            description=
            f'> **`config :`** show\'s the guild ticket pannel configurations.\n\n'
            f'Allows you to create, edit, and delete panel configurations efficiently.'
        )
        embed.set_author(name='panel commands')
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.reply(embed=embed, mention_author=False)

    @panel.command(
        name='config',
    )
    @commands.has_permissions(administrator=True)
    async def panel_add(self, ctx: commands.Context):
        guildData = await self.bot.db.guildconfig.find_unique(
            where={
                'guildId' : ctx.guild.id
            }
        )
        embed = discord.Embed(
            color=config.Color.default,
            description=
            f'**Panels :** {guildData.pannel_count}\n'
            f'**Tickets Created :** {guildData.tickets_created}'
        )
        embed.add_field(
            name='descriptions :',
            value=
            '> **`view   :`** shows the current configurations.\n'
            '> **`add    :`** creates a new ticket panel.\n'
            '> **`remove :`** removes the existing ticket panel.\n'
            '> **`edit   :`** edits the existing panel.'
        )
        embed.set_author(name='Pannel Configurations')
        embed.set_footer(text=ctx.guild.name, icon_url=self.bot.user.default_avatar)
        view = CreatePannelView(bot=self.bot, ctx=ctx)
        await ctx.reply(embed=embed, view=view)

    @commands.group(
        name='config'
    )
    @commands.has_permissions(administrator=True)
    async def guild_configurations(self, ctx: commands.Context):
        guildData = await self.bot.db.guildconfig.find_unique(
            where={
                'guildId' : ctx.guild.id
            }
        )
        embed = discord.Embed(
            color=config.Color.default,
            description=
            f'> **prefix  :** {guildData.prefix}\n'
            f'> **pannels :** {guildData.pannel_count}\n'
            f'> **tickets created :** {guildData.tickets_created}'
        )
        embed.set_author(name=f'{ctx.guild.name}\'s config')
        await ctx.reply(embed=embed, view=None)
        await ctx.reply(embed=embed, view=None)