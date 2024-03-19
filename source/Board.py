import random

class Board:
    def __init__(self, size):
        print(size)
        self.size = size
        self.board = []

        for row in range(self.size[0]):
            row= []
            for col in range(self.size[1]):
                piece = None
                row.append(piece)
            self.board.append(row)
