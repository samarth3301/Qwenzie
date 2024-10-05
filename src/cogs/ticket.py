import discord
from discord.ext import commands
from core.bot import Bot

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
        await ctx.send(embed=embed, mention_author=False)


async def setup(bot: Bot):
    await bot.add_cog(TicketsCog(bot))