import discord


async def say(message):
    await message.delete()
    text = message.content.split(maxsplit=1)[1]
    await message.channel.send(text)
