import random
import discord
import random

async def rtd(message):
    text = message.content.split()[:2]
    if text[0] == "!rtd":
        if len(text) >= 2:
            if text[1].isdigit():
                n = random.randint(1,int(text[1]))
                await message.channel.send(n)
        else:
            n = random.randint(1,6)
            await message.channel.send(n)
