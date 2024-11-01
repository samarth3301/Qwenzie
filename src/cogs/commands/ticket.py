import config
import discord
from discord.ext import commands
from core.bot import Bot
from tools.views.panel import AdminTicketMenu

class TicketsCog(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.hybrid_group(
        name='ticket'
    )
    async def ticket(self, ctx: commands.Context):
        embed = discord.Embed(
            color=self.bot.config.Color.default,
            description=''
        )
        embed.set_author(name='Ticket Commands')
        embed.add_field(
            name='descriptions :',
            value=
            '> **`close      :`** closes the existing ticket.\n'
            '> **`delete     :`** deletes the existing ticket.\n'
            '> **`info       :`** shows the ticket information.\n'
            '> **`transcript :`** transcript\'s the ticket.\n'
        )
        await ctx.send(
            embed=embed,
            mention_author=False
        )

    @commands.command(
        name='config',
    )
    @commands.has_guild_permissions(administrator=True)
    async def config(self, ctx: commands.Context):
        guildData = await self.bot.db.guildconfig.find_first(where={
            "guildId" : int(ctx.guild.id)
        })
        
        if guildData is None:
            guildData = {
                "prefix": "?",
                "pannel_count": 0,
                "tickets_created": 0
            }
        
        embed = discord.Embed(
            color=config.Color.default,
            description=
            f'> **prefix  :** {guildData["prefix"]}\n'
            f'> **pannels :** {guildData["pannel_count"]}\n'
            f'> **tickets created :** {guildData["tickets_created"]}'
        )
        embed.set_author(
            name='Current Guild Configuration'
        )
        embed.add_field(
            name='⚙️ Configuration Guide',
            value=
            f'Select from the buttons below to interact with the panel features.\n'
            f'> **list:** Lists all the ticket panels in this guild.\n'
            f'> **add:** create a new ticket panel.\n'
            f'> **remove:** remove a ticket panel.\n'
        )
        view = AdminTicketMenu(self.bot)
        await ctx.send(
            embed=embed,
            view=view
        )