import discord
from discord.ext import commands
from core.bot import Bot
from utils.logger import logger


class GlobalEvents(commands.Cog):
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
        except Exception as e:
            logger.error(f"Error querying guild configuration: {e}")

async def setup(bot: Bot):
    await bot.add_cog(GlobalEvents(bot))