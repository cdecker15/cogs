from redbot.core import commands

import requests
from bs4 import BeautifulSoup

URL = 'https://warbandtracker.com/goldberg/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.table

a = []
count = 1

for tag in results.find_all('b'):
    a.append(tag.string)


class Viswax(commands.Cog):

    @commands.command()
    async def viswax(self, ctx):
        await ctx.send("First Rune: " + a[0] + "\n" + "Second Rune: " + a[1] + ", " + a[2] + ", " + a[3])