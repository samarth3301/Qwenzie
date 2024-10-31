from core.bot import Bot

from cogs.commands.admin import AdminCog
from cogs.commands.ticket import TicketsCog
from cogs.commands.utils import UtilCog


async def setup(bot: Bot):
    await bot.add_cog(AdminCog(bot))
    await bot.add_cog(TicketsCog(bot))
    await bot.add_cog(UtilCog(bot))
