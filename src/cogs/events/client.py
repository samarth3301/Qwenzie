import config
import discord
from discord.ext import commands
from core.bot import Bot
from utils.logger import logger


class ClientEvents(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        logger.info(f"Guild joined: {guild.id}")
        try:
            guild_check = await self.bot.db.guildconfig.find_unique(where={
                'guildId': int(guild.id),  
            })
            if not guild_check:
                try:
                    await self.bot.db.guildconfig.create(data={
                        'guildId': int(guild.id),
                    })
                except Exception as e:
                    logger.error(f"Error adding guild configuration to the database: {e}")
            hook = discord.SyncWebhook.from_url(self.bot.config.Loggers.guild)
            embed = discord.Embed(
                color=config.Color.default,
                description=
                f'> **Name:** `{guild.name}` ({guild.id})\n'
                f'> **Owner:** `{guild.owner.name}` ({guild.owner.id})\n'
                f'> **Members:** {guild.member_count}\n'
                f'> **Channels:** {len(guild.channels)}\n'
                f'> **Roles:** {len(guild.roles)}\n'
                f'> **Created At:** {guild.created_at.strftime("%d %b %Y %H:%M")}\n'
                f'> **Boosts:** {guild.premium_subscription_count}\n'
                f'> **Vanity:** {guild.vanity_url_code if guild.vanity_url_code else "None"}',
            )
            embed.set_footer(text=f"Guild Count: {len(self.bot.guilds)}")
            if guild.icon:
                embed.set_thumbnail(url=guild.icon.url)
            if guild.banner:
                embed.set_image(url=guild.banner.url)
            hook.send(content=f"⭐ : **Joined A New Guild.**", embed=embed)
        except Exception as e:
            logger.error(f"Error querying guild configuration: {e}")

    @commands.Cog.listener()
    async def on_guild_leave(self, guild: discord.Guild):
        logger.info(f"Guild left: {guild.id}")
        try:
            guild_check = await self.bot.db.guildconfig.find_first(where={
                'guildId': int(guild.id),
            })
            if guild_check:
                try:
                    await self.bot.db.guildconfig.delete(where={
                        'guildId': int(guild.id)
                    })
                except Exception as e:
                    logger.error(f"Error removing guild configuration from the database: {e}")
            hook = discord.SyncWebhook.from_url(self.bot.config.Loggers.guild)
            embed = discord.Embed(
                color=config.Color.default,
                description=
                f'> **Name :** {guild.name} ({guild.id})\n'
                f'> **Owner:** {guild.owner} ({guild.owner.id})'
            )
            embed.set_footer(text=f"Guild Count: {len(self.bot.guilds)}")
            if guild.icon:
                embed.set_thumbnail(url=guild.icon.url)
            if guild.banner:
                embed.set_image(url=guild.banner.url)
            hook.send(content=f"🗑️ : Left A Guild.", embed=embed)
        except Exception as e:
            logger.error(f"Error querying guild configuration: {e}")