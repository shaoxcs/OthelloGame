class Playground:

    def __init__(self, SQUARE, SIZE, STROKE_WEIGHT):
        self.SIZE = SIZE
        self.SQUARE = SQUARE
        self.WIDTH = SQUARE * SIZE
        self.HEIGHT = SQUARE * SIZE
        self.STROKE_WEIGHT = STROKE_WEIGHT

    def display(self):
        strokeWeight(self.STROKE_WEIGHT)
        for i in range(1, self.SIZE):
            line(self.SQUARE*i, 0,
                 self.SQUARE*i, self.HEIGHT)
            line(0, self.SQUARE*i,
                 self.WIDTH, self.SQUARE*i)
