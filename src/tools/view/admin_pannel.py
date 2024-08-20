import config
import discord
from tools.view.create_pannel import AddPannelView
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
            f'Select your preferances from the options below.\n'
            f'And select the save button. To save your changes.\n'
            f'Click next to move to the next customization.\n'
            f'Leave the dropdowns blank to avoid the option.\n'
            f'Click on the `ℹ️` button for more information.'
        )
        view = AddPannelView(self.bot, self.ctx)
        await interation.response.edit_message(embed=embed, view=view)

    @discord.ui.button(label='remove panel', style=discord.ButtonStyle.primary, row=0)
    async def remove_panel_interaction(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(
            color=config.Color.default,
            description='Pannels configurations to be listed here'
        )
        await interaction.response.send_message(embed=embed, ephemeral=True, view=self)

    @discord.ui.button(label='edit panel', style=discord.ButtonStyle.primary, row=0)
    async def edit_panel_interaction(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(
            color=config.Color.default,
            description='Editable Pannels configurations to be listed'
        )
        await interaction.response.send_message(embed=embed, ephemeral=True, view=self)
