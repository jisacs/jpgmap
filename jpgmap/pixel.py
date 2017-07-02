class Pixel():

    UNKNOWN = 0
    ROAD    = 1
    ROCK    = 2

    def __init__(self, x, y):
        """
        param:
            Point, pixel position
        """
        self.x = x
        self.y = y
        self.type = self.UNKNOWN

    def __eq__(self, rhs):
        if self.x == rhs.x and self.y == rhs.y:
            return True
        return False
