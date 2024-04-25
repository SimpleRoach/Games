class players_RPS:

    def __init__(self, name = 'Bot'):
        self.name = name


class Count_RPS:

    def __init__(self, name, bool, count = 0):
        self.name = name
        self.count = count
        self.bool = bool

    def count_RPS(self):
        if self.bool == True:
            self.count +=1
        return self.count

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

