import random
class Board:
    def __init__(self, size):
        self.board = []
        self.size = size
        self.max_tile = self.size[0] * self.size[1]
    
    def bomb_number(self):
        if self.max_tile < 100:
            return random.randint(8, 12)
        elif self.max_tile < 121:
            return random.randint(12, 18)
        elif self.max_tile < 150:
            return random.randint(15, 22)
        else:
            return random.randint(17, 25)

    def is_bomb(self):
        bomb_count = self.bomb_number()
        bomb_positions = random.sample(range(self.size[0] * self.size[1]), bomb_count)  
        for row in range(self.size[1]):
            row_data = []
            for col in range(self.size[0]):
                if row * self.size[0] + col in bomb_positions:
                    piece = True
                else:
                    piece = False
                row_data.append(piece)
            self.board.append(row_data)
        return str(bomb_count)

    def is_bomb_at(self, row, col):
        return self.board[row][col]
