from redbot.core import commands

import asyncio
import urllib.request as request
import json
import random
import time


def un_escape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&amp;", "&")
    s = s.replace("&quot;", "\"")
    s = s.replace("&#039;", "\'")
    return s


class TriviaPlus(commands.Cog):
    @commands.command()
    async def triviaplus(self, ctx: commands.Context, *, amount: str):
        """Trivia Plus!"""

        with request.urlopen('https://opentdb.com/api.php?amount=' + amount) as response:
            source = response.read()
            data = json.loads(source)

        data = data['results']

        choices = []

        for result in data:
            question = un_escape(result['question'])
            correct_answer = un_escape(result['correct_answer'])
            choices.append(correct_answer)
            for answer in result['incorrect_answers']:
                choices.append(un_escape(answer))
                random.shuffle(choices)
            answers_formatted = "";
            for choice in choices:
                answers_formatted += choice + '\n'
            await ctx.send(question + "\n" + answers_formatted)
            time.sleep(10)
            await ctx.send(correct_answer)
