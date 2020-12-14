import discord

async def kill(message, admins, client):
    await message.delete()
    if message.author.id in admins:
        await client.logout()
