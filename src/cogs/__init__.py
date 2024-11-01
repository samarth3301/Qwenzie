from core.bot import Bot

from cogs.commands.admin import AdminCog
from cogs.commands.ticket import TicketsCog
from cogs.commands.utils import UtilCog

from cogs.events.client import ClientEvents


async def setup(bot: Bot):
# commands
    await bot.add_cog(AdminCog(bot))
    await bot.add_cog(TicketsCog(bot))
    await bot.add_cog(UtilCog(bot))

# events
    await bot.add_cog(ClientEvents(bot))