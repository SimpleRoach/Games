import random
from random import randint

class Bot_RPS:
    def __init__(self, mov = 0):
        self.mov = mov
        self.step = 0

    def bot_choose(self):
        if self.mov >= 0:
            self.mov += 1
            self.step = random.randint(1, 3)
            if self.step == 1:
                return "Камень"
            if self.step == 2:
                return "Ножницы"
            if self.step == 3:
                return "Бумага"

class Game_RPS:

    def __init__(self, player_chose, computer_chose):
        self.player_chose = player_chose
        self.computer_chose = computer_chose

    def play(self, defolt = 'Камень'):
        if self.player_chose == self.computer_chose:
            return 'Ничья'
        elif self.player_chose == defolt and self.computer_chose == 'Ножницы':
            return 'Победа'
        elif self.player_chose == 'Ножницы' and self.computer_chose == 'Бумага':
            return 'Победа'
        elif self.player_chose == 'Бумага' and self.computer_chose == defolt:
            return 'Победа'
        else:
            return 'Поражение'

def rps(p_step = 'Камень'):
    bot = Bot_RPS()
    bc = bot.bot_choose()
    game = Game_RPS(p_step, bc)
    return bc, game.play()


# print(random.randint(1, 3))
