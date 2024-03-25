import random
class Board:
    def __init__(self, size):
        self.board = []
        self.size = size
        self.max_tile = self.size[0] * self.size[1]

    def bomb_number(self):
        if self.max_tile < 50:
            return random.randint(3, 5)
        elif self.max_tile < 100:
            return random.randint(8, 12)
        elif self.max_tile < 121:
            return random.randint(12, 18)
        elif self.max_tile < 150:
            return random.randint(15, 22)
        else:
            return random.randint(17, 25)

    def is_bomb(self, row_clicked, col_clicked, bomb_count):
        bomb_positions = random.sample(range(self.size[0] * self.size[1]), bomb_count)  
        for row in range(self.size[1]):
            row_data = []
            for col in range(self.size[0]):
                if row * self.size[0] + col in bomb_positions:
                    bomb = True
                else:
                    bomb = False
                row_data.append(bomb)
            self.board.append(row_data)
        if len(self.board[0])* len(self.board) == self.size[1]*self.size[0]:

            bomb_neighbour = self.check_neighbour(row_clicked, col_clicked)

            if self.is_bomb_at(row_clicked,col_clicked) or bomb_neighbour != 0:
                print("hello")
                self.board = []
                self.is_bomb(row_clicked, col_clicked, bomb_count)

    def is_bomb_at(self, row, col):
        return self.board[row][col]


    def check_neighbour(self, row_clicked, col_clicked):
        bomb_count = 0
        for r in range(-1, 2):
            for c in range(-1, 2):
                if (r != 0 or c != 0) and 0 <= row_clicked + r < self.size[1] and 0 <= col_clicked + c < self.size[0]:
                    if self.is_bomb_at(row_clicked + r, col_clicked + c):
                        bomb_count += 1
        return bomb_count