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

def check_answer(self, answer):
    return True

async def wait_for_answer(self, answer):
    try:
        message = await self.ctx.bot.wait_for(
            "message", check=self.check_answer(answer), timeout=10
        )
    except asyncio.TimeoutError:
        if time.time() - self._last_response >= 10:
            await self.ctx.send(_("Guys...? Well, I guess I'll stop then."))
            self.stop()
            return False
    else:
        self.scores[message.author] += 1
        reply = _("You got it {user}! **+1** to you!").format(user=message.author.display_name)
        await self.ctx.send(reply)
    return True


class TriviaPlus(commands.Cog):
    @commands.command()
    async def triviaplus(self, ctx):
        """Trivia Plus!"""
        with request.urlopen('https://opentdb.com/api.php?amount=1') as response:
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
            continue_ = await self.wait_for_answer()
            await ctx.send(correct_answer)

        await self.ctx.send(_("There are no more questions!"))