from tiles import Tiles

NOTHING = -1
BLACK = 0
WHITE = 255


def test_constructor():
    t = Tiles(8, 100, 90, 60)
    assert t.SQUARE_WIDTH == 100
    assert t.DIAMETER == 90
    assert t.CIRCLE_D == 60
    assert t.valid == [(2, 3), (3, 2), (4, 5), (5, 4)]
    assert t.SIZE == 8
    assert t.black_turn


def test_first_four_tiles():
    t = Tiles(4, 100, 90, 60)
    assert t.tiles[0][0] == NOTHING
    assert t.tiles[1][1] == WHITE


def test_add_tile():
    t = Tiles(4, 100, 90, 60)
    assert t.total_size() == 4
    assert t.black_turn
    t.add_tile(50, 150)
    assert not t.black_turn
    assert t.tiles[1][0] == BLACK
    assert t.black_size == 4


def test_update():
    t = Tiles(4, 100, 90, 60)
    assert (2, 0) not in t.valid
    t.add_tile(50, 150)
    assert (2, 0) in t.valid


def test_total_size():
    t = Tiles(4, 100, 90, 60)
    assert t.total_size() == 4
    t.add_tile(50, 150)
    assert t.total_size() == 5


def test_on_pg():
    t = Tiles(4, 100, 90, 60)
    assert t.on_pg(1, 1)
    assert not t.on_pg(7, 7)


def test_flip():
    t = Tiles(4, 100, 90, 60)
    assert t.tiles[1][1] == t.WHITE
    t.flip(0, 1)
    assert t.tiles[1][1] == t.BLACK
