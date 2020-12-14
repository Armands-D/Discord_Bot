import discord
from time import sleep
from dotenv import load_dotenv

import os

# Commands
from re import *
from rtd import *
from dindins import *
from helpme import *
from vote import *
from kill import *
from say import *
from rem import *
from test import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Armands
admins = {315480446345674753}

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

prefix = "!"
@client.event
async def on_message(message):
    if prefix + "rtd" in message.content:
        await rtd(message)

    if prefix + "dindins" in message.content:
        await dindins(message, admins)
    
    if prefix + "help" in message.content:
        await help_com(message)

    if prefix + "vote" in message.content:
        await vote(message)

    if prefix + "kill" in message.content:
        await kill(message, admins, client)
    
    if prefix + "say" in message.content:
        await say(message)

    if prefix + "rem" in message.content:
        await rem(message, admins)

    if prefix + "w" in message.content:
        if len(message.raw_mentions) == 1:
            p1 = message.author
            p2 = message.mentions[0]
            if p1.id != p2.id:
                if p1.id not in playing and p2.id not in playing:
                    playing[p1.id] = 0
                    playing[p2.id] = 0
                    await bs(p1, p2)

client.run(TOKEN)
