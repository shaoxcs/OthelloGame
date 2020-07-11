from game_controller import GameController
from playground import Playground
from tiles import Tiles


def test_constructor():
    pg = Playground(100, 4, 3)
    ts = Tiles(4, 100, 90, 60)
    gc = GameController(4, 100, pg, ts)
    assert not gc.black_wins
    assert not gc.white_wins
    assert not gc.draw
    assert not gc.score_saved
    assert gc.SQUARE == 100
    assert gc.WIDTH == 400
    assert gc.HEIGHT == 400
    assert gc.time_counter == 0


def test_player_move():
    pg = Playground(100, 4, 3)
    ts = Tiles(4, 100, 90, 60)
    gc = GameController(4, 100, pg, ts)
    gc.player_move(50, 150)
    assert gc.tiles.total_size() == 5


def test_update():
    pg = Playground(100, 4, 3)
    ts = Tiles(4, 100, 90, 60)
    gc = GameController(4, 100, pg, ts)
    gc.player_move(50, 150)
    assert gc.time_counter == 0
    assert not gc.tiles.black_turn
    gc.update()
    assert gc.time_counter == 1


def test_ai_move():
    pg = Playground(100, 4, 3)
    ts = Tiles(4, 100, 90, 60)
    gc = GameController(4, 100, pg, ts)
    gc.player_move(50, 150)
    assert gc.tiles.total_size() == 5
    assert len(gc.tiles.valid) == 3
    gc.ai_move()
    assert gc.tiles.total_size() == 6
