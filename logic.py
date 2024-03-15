import numpy as np

class Logic :
    def __init__(self, size, current_player):
        self.size = size
        self.board = np.zeros((size, size))
        self.sets = {"red" : [], "blue" : []}
        self.boarder = {"red" : {0 : "top", size-1 : "bottom"}, "blue" : {0 : "left", size-1 : "right"}}
        self.current_player = current_player

    def get_neighbours(self, x, y):
        for offset_x, offset_y in [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]:
            if 0 <= x+offset_x < self.size and 0 <= y+offset_y < self.size:
                yield self.board[x+offset_x, y+offset_y]

    def place_token(self, new_color, x, y):
        self.board[x, y] = new_color

    def add_token(self, x, y):
        neighbor_sets = []
        sets = self.sets[self.current_player]
        for neighbor in self.get_neighbors(x,y):
            for set in sets:
                if neighbor in set:
                    neighbor_sets.append(set)
        new_set = {(x, y)}
        while len(neighbor_sets) > 0:
            neighbor_sets[-2] = neighbor_sets[-2].union(neighbor_sets[-1])
            del(neighbor_sets[-1])
        new_set = new_set.union(neighbor_sets[0])
        boarder = self.boarder[self.current_player].get(y)
        if boarder != None :
            new_set.add(boarder)

    def find_winner(self):
        sets = self.sets[self.current_player]
        boarder = self.boarder[self.current_player]
        for set in sets :
            if boarder[0] in set and boarder[self.size-1] in set:
                return self.current_player