class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def xy(self):
        return self.x, self.y
