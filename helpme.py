import discord

info = [
    " ** +rtd {N} **    : Rolls the dice from 1 to N, N = 6",
    " **+dindins @User {N} {S} **    : Spams mentioned user N times, every S seconds. N = 5, S = 5",
    " **+vote**    : Starts a Strawpoll to vote on games to be played. Click the VOTE link to start voting."
]

async def help_com(message):
    if message.content.index("!help") == 0:
        s = "\n\n".join([x for x in info])
        e = discord.Embed(title="Server Commands", description=s)
        await message.channel.send(embed=e)
