class Point():
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'x: {}, y: {}'.format(str(self.x), str(self.y))

    def __eq__(self, rhs):
        if self.x == rhs.x and self.y == rhs.y:
            return True
        return False
