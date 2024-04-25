import random
from random import randint


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

def main(p_step = 'Камень', b_step = 'Камень'):
    game = Game_RPS(p_step, b_step)
    return game.play()



# print(random.randint(1, 3))
