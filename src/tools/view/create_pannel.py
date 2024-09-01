import config
from typing import Any
import discord
from discord.ext import commands
from core.bot import Bot


class SelectPanelChannel(discord.ui.ChannelSelect):
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


class SelectPanelCategory(discord.ui.ChannelSelect):
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

class SelectPanelSupportRoles(discord.ui.RoleSelect):
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

class SelectPanelAdmins(discord.ui.UserSelect):
    def __init__(self):
        super().__init__(
            placeholder='Select your admins for the panel..',
            min_values=1,
            max_values=5,
            row=3
        )
        self.users = []

    async def callback(self, interaction: discord.Interaction):
        self.users.clear()
        for user in self.values:
            self.users.append(user)
        print(self.users)
        await interaction.response.defer()



class AddPannelView(discord.ui.View):
    def __init__(self, bot: Bot, ctx: commands.Context, *, timeout=180):
        super().__init__(timeout=timeout)
        self.bot = bot
        self.ctx = ctx
        self.select_panel_channel = SelectPanelChannel()
        self.select_panel_category = SelectPanelCategory()
        self.select_panel_support_roles = SelectPanelSupportRoles()
        self.select_panel_admins = SelectPanelAdmins()
        self.add_item(self.select_panel_channel)
        self.add_item(self.select_panel_category)
        self.add_item(self.select_panel_support_roles)
        self.add_item(self.select_panel_admins)

    @discord.ui.button(emoji='✅', label='save', style=discord.ButtonStyle.gray, row=4)
    async def on_save(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed =  discord.Embed(
            color=config.Color.default,
            description=
            f'> **Channel :** <#{self.select_panel_channel.channel_id}> ({self.select_panel_channel.channel_id})\n'
            f'> **Category :** {self.select_panel_category.category_id}\n'
            f'> **Support Roles :** {self.select_panel_support_roles.roles_ids}\n'
            f'> **Ticket Admins :** {self.select_panel_admins.users}'
        )
        embed.set_author(name='Created a new panel with following configurations :')
        await self.bot.db.pannels.create(data={
            'guildId' : interaction.guild.id,
            'channel' : self.select_panel_channel.channel_id,
            'supportRoles' : self.select_panel_support_roles.roles_ids,
            'admins' : self.select_panel_admins.users
        })
        await self.bot.db.guildconfig.update(where={
            'guildId' : interaction.guild.id,
        },
        data={
            'pannel_count' : {'increment' : 1}
        })
        button.style = discord.ButtonStyle.green
        button.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji='⏭️', label='next', style=discord.ButtonStyle.gray, row=4)
    async def on_next(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            color=config.Color.default,
            description='moves to the next configuration'
        )
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(emoji='ℹ️', style=discord.ButtonStyle.gray, row=4)
    async def on_info(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            color=config.Color.default
        )
        embed.set_author(name='Pannel DropDown Values.')
        embed.add_field(name='Pannel Channel', value='> This is the channel where the pannel will be posted in.', inline=False)
        embed.add_field(name='Pannel Category', value='> Select a category where the tickets will be created.', inline=False)
        embed.add_field(name='Support Roles', value='> Select the support ticket roles. (only 5 roles can be selected as support roles)', inline=False)
        embed.add_field(name='Pannel Admins', value='> Select the users who are allowed to manage the tickets under this category. (leave blank if None.)', inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

class AddPannel2View(discord.ui.View):
    pass