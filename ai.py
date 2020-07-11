from random import randint
from tiles import Tiles
from copy import deepcopy


class Ai:

    def __init__(self, SIZE, SQUARE):
        self.SIZE = SIZE
        self.ai_pos = (0, 0)
        self.SQUARE = SQUARE

    def make_random_move(self, tiles):
        ai_index = randint(0, len(tiles.valid) - 1)
        self.ai_pos = tiles.valid[ai_index]
        return self.ai_pos

    def make_greedy_move(self, tiles):
        """
        If ai can move at the corners of board, put tile
        Otherwise, calculate all possible tiles can flip
        Always choose the move flipping the most number of times
        """
        CORNER = [(0, 0), (0, self.SIZE - 1),
                  (self.SIZE - 1, 0), (self.SIZE - 1, self.SIZE - 1)]
        SPECIAL_POS = -1
        greedy_moves = []
        for pos in CORNER:
            if pos in tiles.valid:
                greedy_moves.append((pos, SPECIAL_POS))
        if greedy_moves == []:
            pos_and_num = {}
            max_num = 0
            for (r, c) in tiles.valid:
                num = tiles.refresh(r, c, False)
                pos_and_num[(r, c)] = num
                max_num = max(max_num, num)
            greedy_moves = list(filter(lambda x: x[1] == max_num,
                                       list(pos_and_num.items())))
        ai_index = randint(0, len(greedy_moves) - 1)
        self.ai_pos = greedy_moves[ai_index][0]
        return self.ai_pos
