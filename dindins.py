import discord
from time import sleep
from re import findall


async def dindins(message, admins):
    if len(message.mentions) == 1:
        
        victim = message.mentions[0]
        if victim.id not in admins:
            n = findall(r"\b\d{1,2}\b",message.content)
            if len(n) == 2:
                tmp = n[-2:]
                for inc in range(0,int(tmp[0])):
                    await message.channel.send("Wake up <@%s>!!!" % victim.id)
                    sleep(int(tmp[1]))
            else:
                for inc in range(0,5):
                    await message.channel.send("Wake up <@%s>!!!" % victim.id)
                    sleep(int(5))           
