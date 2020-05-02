from redbot.core import commands

import requests
from bs4 import BeautifulSoup

import urllib.request as request
import json

a = []


def pullVis():
    URL = 'https://warbandtracker.com/goldberg/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.table

    for tag in results.find_all('b'):
        a.append(tag.string)


class Viswax(commands.Cog):

    @commands.command()
    async def viswax(self, ctx):
        """Checks the daily viswax combinations in Runescape."""
        pullVis()
        await ctx.send("First Rune: " + a[0] + "\n" + "Second Rune: " + a[1] + ", " + a[2] + ", " + a[3])

    @commands.command()
    async def myviswax(self, ctx: commands.Context, *, words: str):
        """Calculates the cost of your daily viswax combinations in Runescape."""
        pullVis()
        total1 = 0
        total2 = 0
        total3 = 0
        total1 += calc_cost(a[0])
        total1 += calc_cost(a[1])
        total2 += calc_cost(a[0])
        total2 += calc_cost(a[2])
        total3 += calc_cost(a[0])
        total3 += calc_cost(a[3])

        with request.urlopen(
                'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=32092') as response:
            source = response.read()
            data = json.loads(source)

        viswax_cost = data['item']['current']['price']

        if 'k' in viswax_cost:
            viswax_cost = viswax_cost[:-1]
            viswax_cost = float(viswax_cost) * 1000

        viswax_cost = int(viswax_cost) * 100
        await ctx.send(words)
