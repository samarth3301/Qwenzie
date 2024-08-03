from typing import Any
import discord
from discord.ext import commands


class SelectPannelChannel(discord.ui.ChannelSelect):
    def __init__(self):
        super().__init__(
            channel_types=[discord.ChannelType.text],
            placeholder='Select your pannel channel.',
            min_values=1,
            max_values=1,
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
            max_values=5
        )
        self.roles_ids = []
    
    async def callback(self, interaction: discord.Interaction):
        self.roles_ids.clear()
        for role in self.values:
            self.roles_ids.append(role.id)
        print(self.roles_ids)
        await interaction.response.defer()