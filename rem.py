import discord

async def rem(message, admins):
    if message.author.id in admins:
        await message.delete()
        await message.delete()
