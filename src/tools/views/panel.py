import config
import discord
from core.bot import Bot

class AdminTicketMenu(discord.ui.View):
    def __init__(self, bot: Bot, timeout: int = 100):
        super().__init__(timeout=timeout)
        self.bot = bot

    @discord.ui.button(
        label='list',
        custom_id='list_panel',
        style=discord.ButtonStyle.primary,
        row=0
    )
    async def create_ticket(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.send_message(
            content='List of ticket panels.',
            ephemeral=True
        )

    @discord.ui.button(
        label='add',
        custom_id='add_panel',
        style=discord.ButtonStyle.green,
        row=0
    )
    async def add_panel(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(
        label='remove',
        custom_id='remove_panel',
        style=discord.ButtonStyle.red,
        row=0
    )
    async def remove_panel(self, interaction: discord.Interaction, button: discord.Button):
        pass

    @discord.ui.button(
        emoji="❌",
        custom_id='close',
        style=discord.ButtonStyle.danger,
        row=0
    )
    async def close(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.edit_message(view=None, content='Interaction Closed.')