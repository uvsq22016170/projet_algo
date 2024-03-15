import numpy as np

class Logic :
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size))

    def get_neighbours(self, x, y):
        for offset_x, offset_y in [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]:
            if 0 <= x+offset_x < self.size and 0 <= y+offset_y < self.size:
                yield self.board[x+offset_x, y+offset_y]

    def place_token(self, new_color, x, y):
        self.board[x, y] = new_color