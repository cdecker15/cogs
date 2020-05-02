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

def calc_cost(rune):
    amount = 0
    item_id = 0
    if rune == "Mind Rune":
        amount = 2000
        item_id = 558
    if rune == "Body Rune":
        amount = 2000
        item_id = 559
    if rune == "Air Rune":
        amount = 1000
        item_id = 556
    if rune == "Water Rune":
        amount = 1000
        item_id = 555
    if rune == "Earth Rune":
        amount = 1000
        item_id = 557
    if rune == "Fire Rune":
        amount = 1000
        item_id = 554
    if rune == "Dust Rune":
        amount = 500
        item_id = 4696
    if rune == "Lava Rune":
        amount = 500
        item_id = 4699
    if rune == "Mist Rune":
        amount = 500
        item_id = 4695
    if rune == "Smoke Rune":
        amount = 500
        item_id = 4697
    if rune == "Steam Rune":
        amount = 500
        item_id = 4694
    if rune == "Chaos Rune":
        amount = 500
        item_id = 562
    if rune == "Cosmic Rune":
        amount = 400
        item_id = 564
    if rune == "Death Rune":
        amount = 400
        item_id = 560
    if rune == "Nature Rune":
        amount = 350
        item_id = 561
    if rune == "Blood Rune":
        amount = 350
        item_id = 565
    if rune == "Mud Rune":
        amount = 300
        item_id = 4698
    if rune == "Law Rune":
        amount = 300
        item_id = 563
    if rune == "Astral Rune":
        amount = 300
        item_id = 9075
    if rune == "Soul Rune":
        amount = 300
        item_id = 566

    with request.urlopen(
            'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(item_id)) as response:
        source = response.read()
        data = json.loads(source)

    return int((data['item']['current']['price']) * amount)


class Viswax(commands.Cog):

    @commands.command()
    async def viswax(self, ctx):
        """Checks the daily viswax combinations in Runescape."""
        pullVis()
        await ctx.send("First Rune: " + a[0] + "\n" + "Second Rune: " + a[1] + ", " + a[2] + ", " + a[3])

    @commands.command()
    async def myviswax(self, ctx: commands.Context, *, word: str):
        """Calculates the cost of your daily viswax combinations in Runescape."""
        pullVis()
        total1 = 0
        total2 = 0
        total3 = 0
        total1 += calc_cost(a[0])
        total2 = total1
        total3 = total1
        total1 += calc_cost(a[1])
        total2 += calc_cost(a[2])
        total3 += calc_cost(a[3])

        word = word.capitalize()
        word = word + " Rune"

        total1 += calc_cost(word)
        total2 += calc_cost(word)
        total3 += calc_cost(word)

        with request.urlopen(
                'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=32092') as response:
            source = response.read()
            data = json.loads(source)

        viswax_cost = data['item']['current']['price']

        if 'k' in viswax_cost:
            viswax_cost = viswax_cost[:-1]
            viswax_cost = float(viswax_cost) * 1000

        viswax_cost = int(viswax_cost) * 100
        await ctx.send("First Rune: " + a[0] + "\n" + "Second Rune: " + a[1] + ", " + a[2] + ", " + a[3] + "\nCost of Possibility 1: " + str(total1) + "\nCost of Possibility 2: " + str(total2) + "\nCost of Possibility 3: " + str(total3) +"\nViswax (100) at today's price: " + str(viswax_cost))
