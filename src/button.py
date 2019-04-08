import pyxel
from src import constans as CONST
from src.vector2 import Vec2


class PadButton:
    _SIZE = 5

    def __init__(self, pos, type=0, *, radius=None, width=None, height=None):
        self._type = type
        self._types = (
            self.draw_rect,
            self.draw_circ
        )

        self._pos = pos
        self._is_pressed = False
        self._color = CONST.COLOR.RED
        self.radus = self._SIZE if not radius else radius
        self.width = self._SIZE * 2 if not width else width
        self.height = self._SIZE if not height else height

    @property
    def x(self):
        return self._pos.x

    @x.setter
    def x(self, value):
        self._pos.x = value

    @property
    def y(self):
        return self._pos.y

    @y.setter
    def y(self, value):
        self._pos.y = value

    @property
    def xy(self):
        return self._pos.xy

    def press(self):
        if not self._is_pressed:
            self._is_pressed = True
            self._pos.x += 1
            self._pos.y += 1
            self._color = CONST.COLOR.GREEN

    def release(self):
        if self._is_pressed:
            self._is_pressed = False
            self._pos.x -= 1
            self._pos.y -= 1
            self._color = CONST.COLOR.RED

    def draw(self):
        fun = self._types[self._type]
        fun()

    def draw_rect(self):
        fix_x, fix_y = self._pos.x - self.width // 2, self._pos.y - self.height // 2

        pyxel.rect(fix_x - 1, fix_y - 1,
                   fix_x + self.width + 1, fix_y + self.height + 1,
                   CONST.COLOR.BLACK)

        if not self._is_pressed:
            pyxel.rect(fix_x, fix_y,
                       fix_x + self.width + 2, fix_y + self.height + 2,
                       CONST.COLOR.BLACK)

        pyxel.rect(fix_x, fix_y,
                   fix_x + self.width, fix_y + self.height,
                   self._color)

    def draw_circ(self):
        pyxel.circ(self._pos.x,
                   self._pos.y,
                   self.radus + 1, CONST.COLOR.BLACK)

        if not self._is_pressed:
            pyxel.circ(self._pos.x + 1,
                       self._pos.y + 1,
                       self.radus + 1, CONST.COLOR.BLACK)

        pyxel.circ(self._pos.x,
                   self._pos.y,
                   self.radus, self._color)
