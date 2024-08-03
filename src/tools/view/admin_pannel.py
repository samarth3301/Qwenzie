import config
import discord
from tools.default_view import DefaultView
from discord.ext import commands
from core.bot import Bot


class CreatePannelView(discord.ui.View):
    def __init__(self, *, bot: Bot, ctx: commands.Context, timeout=180):
        super().__init__(timeout=timeout)
        self.bot = bot
        self.ctx = ctx

    @discord.ui.button(label='view panels', style=discord.ButtonStyle.primary, row=0)
    async def pannels_interaction(self, interaction: discord.Interaction, button: discord.Button):
        pannels = await self.bot.db.pannels.find_many(
            where={
                'guildId': self.ctx.guild.id,
            }
        )
        if not pannels:
            description = "No panels found for this guild."
        else:
            panel_ids = [pannel.pannelId for pannel in pannels]
            description = ', '.join(map(str, panel_ids))
        embed = discord.Embed(
            color=config.Color.default,
            description=description
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label='add panel', style=discord.ButtonStyle.primary, row=0)
    async def add_pannel_interaction(self, interation: discord.Interaction, button: discord.Button):
        embed = discord.Embed(
            color=config.Color.default,
            description=
            f'Select your preferances from the options below... and select the save button...'
        )
        await interation.response.edit_message(embed=embed, ephemeral=True)