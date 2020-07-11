from playground import Playground


def test_constructor():
    """Test the constructor"""
    pg = Playground(100, 8, 3)
    assert pg.SIZE == 8
    assert pg.SQUARE == 100
    assert pg.WIDTH == 800
    assert pg.HEIGHT == 800
    assert pg.STROKE_WEIGHT == 3
