import config
import discord
from tools.default_view import DefaultView
from discord.ext import commands


class ConfirmationView(DefaultView):
    def __init__(self, ctx: commands.Context, *, timeout=180):
        super().__init__(ctx, timeout=timeout)
        self.value = None

    @discord.ui.button(label='confirm', style=discord.ButtonStyle.green)
    async def on_confirm(self, interaction: discord.Interaction, button: discord.Button):
        self.value = True
        self.stop()

    @discord.ui.button(label='cancel', style=discord.ButtonStyle.red)
    async def on_cancel(self, interaction: discord.Interaction, button: discord.Button):
        self.value = False
        self.stop()