from redbot.core import commands

class Viswax(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def viswax(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")