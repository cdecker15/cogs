from .viswax.py import Viswax


def setup(bot):
    cog = Viswax(bot)
    bot.add_cog(cog)