import config
from typing import Any
import discord
from discord.ext import commands
from tools.default_view import DefaultView
from src.core.bot import Bot


class SelectPannelChannel(discord.ui.ChannelSelect):
    def __init__(self):
        super().__init__(
            channel_types=[discord.ChannelType.text],
            placeholder='Select your pannel channel.',
            min_values=1,
            max_values=1,
            row=0
        )
        self.channel_id = None
    
    async def callback(self, interaction: discord.Interaction):
        self.channel_id = self.values[0].id
        await interaction.response.defer()


class SelectPannelCategory(discord.ui.ChannelSelect):
    def __init__(self):
        super().__init__(
            channel_types=[discord.ChannelType.category],
            placeholder='Select your ticket category',
            min_values=1,
            max_values=1,
            row=1
        )
        self.category_id = None

    
    async def callback(self, interaction: discord.Interaction):
        self.category_id = self.values[0].id
        await interaction.response.defer()

class SelectPannelSupportRoles(discord.ui.RoleSelect):
    def __init__(self):
        super().__init__(
            placeholder='Select your support roles for the panel..',
            min_values=1,
            max_values=5,
            row=2
        )
        self.roles_ids = []
    
    async def callback(self, interaction: discord.Interaction):
        self.roles_ids.clear()
        for role in self.values:
            self.roles_ids.append(role.id)
        print(self.roles_ids)
        await interaction.response.defer()


class AddPannelView(discord.ui.View):
    def __init__(self, bot: Bot, ctx: commands.Context, *, timeout=180):
        super().__init__(timeout=timeout)
        self.bot = bot
        self.ctx = ctx
        self.add_item(SelectPannelChannel())
        self.add_item(SelectPannelCategory())
        self.add_item(SelectPannelSupportRoles())

    @discord.ui.button(emoji='✅', label='save', style=discord.ButtonStyle.gray, row=3)
    async def on_save(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed =  discord.Embed(
            color=config.Color.default,
            description=
            f'> '
        )
        embed.set_author(name=interaction.guild.icon.url)
        await self.bot.db.pannels.create(
            
        )
        await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(emoji='ℹ️', style=discord.ButtonStyle.gray, row=3)
    async def on_info(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass