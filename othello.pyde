from game_controller import GameController
from playground import Playground
from tiles import Tiles


SQUARE_WIDTH = 100
SIZE = 8
DIAMETER = 90
CIRCLE_D = 40
COLOR_MAX = 255
STROKE_WEIGHT = 3
GREEN = (20, 140, 45)

RANDOM_AI = False
GREEDY_AI = True

tiles = Tiles(SIZE, SQUARE_WIDTH, DIAMETER, CIRCLE_D)
pg = Playground(SQUARE_WIDTH, SIZE, STROKE_WEIGHT)
gc = GameController(SIZE, SQUARE_WIDTH, pg, tiles, RANDOM_AI, GREEDY_AI)


def setup():
    size(SQUARE_WIDTH*SIZE, SQUARE_WIDTH*SIZE)
    colorMode(RGB, COLOR_MAX)


def draw():
    background(*GREEN)
    gc.display()
    gc.update()


def mousePressed():
    gc.player_move(mouseX, mouseY)
