import discord
from time import sleep

playing = {}
discord_emojis = {
    " " : " :ocean: ",
    1 : ":one:",
    2 : ":two:",
    3 : ":three:",
    4 : ":four:",
    5 : ":five:",
    6 : ":six:",
    7 : ":seven:",
    8 : ":eight:"

}

class Board(object):
    top = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def __init__(self):
        self.a = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.b = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.c = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.d = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.c = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.d = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.e = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.f = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.g = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.h = [" ", " ", " ", " ", " ", " ", " ", " "]
        self.full = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h]

    def return_board(self):
        s = "  " + " ".join(Board.top)
        sep = "\n  " + "─" * 16 + "\n"
        s += sep
        i = 0
        for item in self.full:
            s += Board.top[i]
            s += "|" + "|".join(item) + "|" + sep
            i += 1
        return s

    def discordify(self):
        s = self.return_board()
        s = s.replace(" ", " " * 5) # " " * 5
        return s



class Ship4(object):
    def __init__(self):
        self.length = 4
        self.pos = ["", "", "", ""]
        self.status = "live"

class Ship3(object):
    def __init__(self):
        self.length = 3
        self.pos = ["", "", ""]
        self.status = "live"

class Ship2(object):
    def __init__(self):
        self.length = 2
        self.pos = ["", "",]
        self.status = "live"

class Ship2(object):
    def __init__(self):
        self.length = 1
        self.pos = [""]
        self.status = "live"

    def __str__(self):
        return ":ship:"




async def bs(p1, p2):

    board = Board()

    if p1.dm_channel is None:
        await p1.create_dm()
        p1_msg = await p1.dm_channel.send(board.discordify())
    else:
        p1_msg = await p1.dm_channel.send(board.discordify())
    
    # if p2.dm_channel is None:
    #     await p2.create_dm()
    #     p2_msg = await p2.dm_channel.send("WOAH")
    # else:
    #     p2_msg = await p2.dm_channel.send("WOAH")

    # example await p1_msg.edit(content = "WOAH")

    p1_b = Board()
    async def on_message(message):
        if message.content == "123":
            message.send("WOAH")
