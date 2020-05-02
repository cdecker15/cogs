from redbot.core import commands

import urllib.request as request
import json
import random


class Viswax(commands.Cog):

    @commands.command()
    async def triviaplus(self, ctx):
        """Checks the daily viswax combinations in Runescape."""
        await ctx.send("...")