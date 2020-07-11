DIRECTION = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
NOTHING = -1
BLACK = 0
WHITE = 255


class Tiles:

    def __init__(self, SIZE, SQUARE_WIDTH, DIAMETER, CIRCLE_D):
        self.SQUARE_WIDTH = SQUARE_WIDTH
        self.DIAMETER = DIAMETER
        self.CIRCLE_D = CIRCLE_D
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.NOTHING = NOTHING
        self.valid = []
        self.SIZE = SIZE
        self.tiles = [[self.NOTHING] * SIZE for i in range(SIZE)]
        self.first_four_tiles()
        self.black_turn = True
        self.update()

    def first_four_tiles(self):
        LEFT_MID = self.SIZE // 2 - 1
        RIGHT_MID = self.SIZE // 2
        self.tiles[LEFT_MID][LEFT_MID] = self.WHITE
        self.tiles[RIGHT_MID][RIGHT_MID] = self.WHITE
        self.tiles[LEFT_MID][RIGHT_MID] = self.BLACK
        self.tiles[RIGHT_MID][LEFT_MID] = self.BLACK
        self.black_size = 2
        self.white_size = 2

    def add_tile(self, x, y):
        col = x // self.SQUARE_WIDTH
        row = y // self.SQUARE_WIDTH
        if (row, col) in self.valid:
            if self.black_turn:
                self.tiles[row][col] = self.BLACK
                self.black_size += 1
            else:
                self.tiles[row][col] = self.WHITE
                self.white_size += 1
            self.refresh(row, col, True)
            self.black_turn = not self.black_turn
            self.update()

    def update(self):
        del(self.valid[:])
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                self.refresh(row, col)
        self.say_turn()

    def refresh(self, row, col, flip=False):
        if self.black_turn:
            cur_color = self.BLACK
            opp_color = self.WHITE
        else:
            cur_color = self.WHITE
            opp_color = self.BLACK
        posible_flip_num = 0
        for (ori_r, ori_c) in DIRECTION:
            dis = 1
            n_row = row + ori_r * dis
            n_col = col + ori_c * dis
            should_flip = []
            while (self.on_pg(n_row, n_col)
                   and self.tiles[n_row][n_col] == opp_color):
                should_flip.append((n_row, n_col))
                dis += 1
                n_row = row + ori_r * dis
                n_col = col + ori_c * dis
                if (not self.on_pg(n_row, n_col) or
                   self.tiles[n_row][n_col] == self.NOTHING):
                    break
                elif self.tiles[n_row][n_col] == cur_color:
                    posible_flip_num += len(should_flip)
                    if flip:
                        self.flip_list(should_flip, cur_color)
                        break
                    elif (self.tiles[row][col] == self.NOTHING and
                          (row, col) not in self.valid):
                        self.valid.append((row, col))
                        break
        return posible_flip_num

    def flip_list(self, positions, cur_color):
        for (r, c) in positions:
            self.tiles[r][c] = cur_color
            if self.black_turn:
                self.black_size += 1
                self.white_size -= 1
            else:
                self.white_size += 1
                self.black_size -= 1

    def on_pg(self, row, col):
        return (0 <= row and row < self.SIZE
                and 0 <= col and col < self.SIZE)

    def total_size(self):
        return self.black_size + self.white_size

    def say_turn(self):
        if self.black_turn:
            print('Player turn!')
        else:
            print('AI turn!')

    def display(self):
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if self.tiles[row][col] != self.NOTHING:
                    fill(self.tiles[row][col])
                    ellipse((col+0.5) * self.SQUARE_WIDTH,
                            (row+0.5) * self.SQUARE_WIDTH,
                            self.DIAMETER, self.DIAMETER)
