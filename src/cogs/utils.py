import config
import discord
from core.bot import Bot
from discord.ext import commands

class UtilCommands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(
        name='ping'
    )
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'🏓 Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(
        name='links',
        aliases=['support', 'info']
    )
    async def links(self, ctx: commands.Context):
        embed = discord.Embed(
            color=self.bot.config.Color.default,
            description=
            'Hi, I am Qwenzie.\n'
            f'A adorable discord bot. Capable to manage your servers with ease.\n'
            f'You can invite me to your server by clicking on the Invite button below.\n'
            f'If you need any help or support, you can join my support server by clicking on the Support Server button below.'
            f'If you have any suggestions or feedback, you can join my support server and share your thoughts.'
        )
        embed.set_footer(text=f'requested by {ctx.author.name}', icon_url=ctx.author.display_avatar)
        embed.set_author(name='Qwenzie', icon_url=self.bot.user.avatar_url)
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label='Support Server', url=self.bot.config.Links.support, style=discord.ButtonStyle.link))
        view.add_item(discord.ui.Button(label='Invite Me', url=self.bot.config.Links.invite, style=discord.ButtonStyle.link))
        await ctx.reply(view=view, embed=embed)


async def setup(bot: Bot):
    bot.add_cog(UtilCommands(bot))