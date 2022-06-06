from chess import Chess
from random import choice as chc

emojis = {
    'dark':981574100952694794,
    'light':981574079280717825,
    'bkd': 981556532288323685,
    'bkl': 981565611001921576,
    'bqd': 981564324172673055,
    'bql': 981565692094607440,
    'bnd': 981564678616547358,
    'bnl': 981565817814663189,
    'bbd': 981564604037595216,
    'bbl': 981565755227275354,
    'brd': 981565437106077756,
    'brl': 981565889629536267,
    'bpd': 981565531154960414,
    'bpl': 981565947649347594,
    'wkd': 981569115514880101,
    'wkl': 981569197547085905,
    'wqd': 981569090479063051,
    'wql': 981569235245473852,
    'wnd': 981569325246865438,
    'wnl': 981569346558103623,
    'wbd': 981569264035196989,
    'wbl': 981569289020666007,
    'wrd': 981569368628543498,
    'wrl': 981569402250068021,
    'wpd': 981569425100644443,
    'wpl': 981569448676835358
}

import nextcord

bot = nextcord.Client()


game = None

mess = None

class Game:
    def __init__(self, plr1, plr2):
        self.black = chc((plr1, plr2))
        self.white = plr2 if self.black == plr1 else plr1
        self.turn = chc(("black", "white"))
        self.chess = Chess()

    def redraw(self):
        cb = self.chess.cb
        string = ':one::two::three::four::five::six::seven::eight:\n'
        adder = 0
        for k,v in enumerate(cb):
            emoji_name = ""
            bg = 'd' if (k+adder)%2 == 0 else 'l'
            if v == 0:
                emoji_name = 'dark' if bg == 'd' else 'light'       
            else:
                if str(v)[1] =='1':
                    typ = 'p'
                if str(v)[1] =='2':
                    typ = 'b'
                if str(v)[1] =='3':
                    typ = 'n'
                if str(v)[1] =='4':
                    typ = 'r'
                if str(v)[1] =='5':
                    typ = 'q'
                if str(v)[1] =='6':
                    typ = 'k'

                clr = 'b' if str(v)[0] == '2' else 'w'
                emoji_name = clr+typ+bg
            
            string += f'<:{emoji_name}:{emojis[emoji_name]}>'
            
            abc = ['a','b','c','d','e','f','g','h']
            if (k+1)%8 == 0:
                string += f':regional_indicator_{abc[int(k/8)]}:\n'
                adder += 1

        return string

    def make_move(self, tile, move):
        cb = self.chess.cb
        check = '2' if self.turn == 'black' else '1'
        if cb[tile] == 0:
            return 'ERROR: there is no chesspiece in that tile'
        elif str(cb[tile])[0] != check:
            return 'ERROR: that is not your chesspiece'
        else:    
            done = self.chess.make_move(tile, move)
            if done:
                self.turn = 'black' if self.turn == 'white' else 'white'
                return False
            else:
                return 'ERROR: that is not a valid move'

    def get_tile(self, tile):
        abc = ['a','b','c','d','e','f','g','h']
        return 8 * abc.index(tile[1]) + int(tile[0]) - 1

@bot.event
async def on_ready():
    print('bot ready')

@bot.event
async def on_message(message):
    global game, mess
    if message.content[:6] == '!start':
        if len(message.content) == 6:
            await message.channel.send('please mention the opponent')
        else:
            plr1 = message.author.id
            plr2 = message.content[9:9+18]
            game = Game(plr1, plr2)
            await message.channel.send('**GAME HAS STARTED!!!**')
            mess = await message.channel.send(game.redraw())
            await message.channel.send(f"<@{game.black}> is black\n<@{game.white}> is white\n Its {game.turn}'s turn now")
    elif message.content[:6] == "!emoji":
        emoji = message.content[7:]
        print(emoji)
        await message.channel.send(emoji)
    elif game:
        splitted = message.content.split('>')
        worked = game.make_move(game.get_tile(splitted[0]), game.get_tile(splitted[1]))
        if not worked:
            await mess.edit(game.redraw())
        else:
            await message.channel.send(worked)


bot.run(token)
