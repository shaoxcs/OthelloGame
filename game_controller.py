from ai import Ai

GOLDEN = (255, 215, 0)
TEXT_SIZE = 50
HALF_THE_LEN = 2


class GameController:

    def __init__(self, SIZE, SQUARE, playground, tiles, RANDOM_AI, GREEDY_AI):
        self.black_wins = False
        self.white_wins = False
        self.draw = False
        self.SIZE = SIZE
        self.WIDTH = SIZE * SQUARE
        self.HEIGHT = SIZE * SQUARE
        self.SQUARE = SQUARE
        self.pg = playground
        self.tiles = tiles
        self.time_counter = 0
        self.score_saved = False
        self.random_ai = RANDOM_AI
        self.greedy_ai = GREEDY_AI
        self.minimax = False

    def player_move(self, x, y):
        if self.tiles.black_turn:
            self.tiles.add_tile(x, y)
            self.time_counter = 0

    def ai_move(self):
        ai = Ai(self.SIZE, self.SQUARE)
        if self.greedy_ai:
            ai_pos = ai.make_greedy_move(self.tiles)
        elif self.random_ai:
            ai_pos = ai.make_random_move(self.tiles)
        ai_pos_x = ai_pos[1] * self.SQUARE + self.SQUARE // HALF_THE_LEN
        ai_pos_y = ai_pos[0] * self.SQUARE + self.SQUARE // HALF_THE_LEN
        self.tiles.add_tile(ai_pos_x, ai_pos_y)

    def update(self):
        REFRESH_TIMES = 60
        UPDATE_ONE_REFRESH = 1
        AI_DELAY = 1
        if self.tiles.valid == []:
            self.draw = self.tiles.white_size == self.tiles.black_size
            self.black_wins = self.tiles.black_size > self.tiles.white_size
            self.white_wins = self.tiles.black_size < self.tiles.white_size
            self.get_player_name()
            self.anounce()
            self.save_score()
        elif not self.tiles.black_turn:
            self.time_counter += UPDATE_ONE_REFRESH
            if self.time_counter == AI_DELAY * REFRESH_TIMES:
                self.ai_move()
                self.time_counter = 0

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def get_player_name(self):
        if not self.score_saved:
            player_name = self.input('enter your name')
            if player_name:
                print('hi ' + player_name)
            elif player_name == '':
                print('[empty string]')
            else:
                print(player_name)
            self.player = player_name

    def save_score(self):
        if not self.score_saved:
            records = []
            with open('scores.txt') as f:
                for line in f:
                    name_and_score = line.split()
                    records.append((name_and_score[0], int(name_and_score[1])))
            if records != [] and self.tiles.black_size >= records[0][1]:
                records.insert(0, (self.player, self.tiles.black_size))
            else:
                records.append((self.player, self.tiles.black_size))
            with open('scores.txt', 'w') as f:
                for record in records:
                    f.write(record[0] + " " + str(record[1]) + "\n")
            self.score_saved = True

    def anounce(self):
        WINNER_POS_HOR = self.WIDTH / 2 - 180
        WINNER_POS_VER = self.WIDTH / 2
        LEFT_POS = self.WIDTH * 1 / 5
        RIGHT_POS = self.WIDTH * 3 / 5
        VERTICAL_POS = self.HEIGHT * 5 / 8
        fill(*GOLDEN)
        textSize(TEXT_SIZE)
        if self.white_wins:
            if self.random_ai:
                text("Random AI Wins", WINNER_POS_HOR, WINNER_POS_VER)
            else:
                text("Greedy AI Wins", WINNER_POS_HOR, WINNER_POS_VER)
        elif self.black_wins:
            text(self.player + " Wins", WINNER_POS_HOR, WINNER_POS_VER)
        elif self.draw:
            text("DRAW", WINNER_POS_HOR, WINNER_POS_VER)
        text("Black " + str(self.tiles.black_size), LEFT_POS, VERTICAL_POS)
        text("White " + str(self.tiles.white_size), RIGHT_POS, VERTICAL_POS)

    def display(self):
        self.tiles.display()
        self.pg.display()
        self.show_ai()

    def show_ai(self):
        AI_POS_HOR = self.WIDTH / 2 - 200
        AI_POS_VER = self.HEIGHT / 2
        if self.time_counter != 0:
            fill(*GOLDEN)
            textSize(TEXT_SIZE)
            if self.random_ai:
                text("Random AI thinking", AI_POS_HOR, AI_POS_VER)
            else:
                text("Greedy AI thinking", AI_POS_HOR, AI_POS_VER)

