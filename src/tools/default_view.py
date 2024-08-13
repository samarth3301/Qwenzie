import config
import discord
from discord.ext import commands
from discord.ui import View


class DefaultView(View):
    def __init__(self, ctx: commands.Context, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.ctx = ctx


    async def interaction_check(self, interaction: discord.Interaction[discord.Client]):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message(
                embed=discord.Embed(
                    color=config.Colors.default,
                    description=f'{config.Emojies.cross} {interaction.user.mention} : Looks like this interaction cannot be controlled by you.'
                ),
                ephemeral=True,
                delete_after=5
            )
            return False
        return True
    
    async def on_timeout(self):
        for child in self.children:
            child.disable = True
            try:
                await self.message.edit(view=self)
            except:
                pass
