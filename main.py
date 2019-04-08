import pyxel
from src.vector2 import Vec2
from src.button import PadButton
from src import constans as CONST


class GamePadImage:
    __IMAGE_POS_X = 0
    __IMAGE_POS_Y = 0
    __WIDHT = 135
    __HEIGHT = 50

    POS_X = 0
    POS_Y = 0
    __POS_ON_WINDOW_X = POS_X - __WIDHT // 2
    __POS_ON_WINDOW_Y = POS_Y - __HEIGHT // 2

    @classmethod
    def move(cls, x, y):
        cls.POS_X = x
        cls.POS_Y = y
        cls.__POS_ON_WINDOW_X = x - cls.__WIDHT // 2
        cls.__POS_ON_WINDOW_Y = y - cls.__HEIGHT // 2

    @classmethod
    def draw(cls):
        pyxel.blt(cls.__POS_ON_WINDOW_X, cls.__POS_ON_WINDOW_Y,
                  0,
                  cls.__IMAGE_POS_X, cls.__IMAGE_POS_Y,
                  cls.__WIDHT, cls.__HEIGHT
                  )


class Window:

    def __init__(self):
        pyxel.init(CONST.WINDOW.WIDTH, CONST.WINDOW.HEIGHT,
                   caption=CONST.WINDOW.TITLE)
        pyxel.load("assets/assets.pyxel")
        pyxel.mouse(True)

        self.buttons = {
            pyxel.GAMEPAD_1_A: PadButton(Vec2(0, 0), 1, radius=4),
            pyxel.GAMEPAD_1_B: PadButton(Vec2(0, 0), 1, radius=4),
            pyxel.GAMEPAD_1_X: PadButton(Vec2(0, 0), 1, radius=4),
            pyxel.GAMEPAD_1_Y: PadButton(Vec2(0, 0), 1, radius=4),
            pyxel.GAMEPAD_1_LEFT_SHOULDER: PadButton(Vec2(0, 0), 0, width=15, height=3),
            pyxel.GAMEPAD_1_RIGHT_SHOULDER: PadButton(Vec2(0, 0), 0, width=15, height=3),
            pyxel.GAMEPAD_1_SELECT: PadButton(Vec2(0, 0), 0, height=3),
            pyxel.GAMEPAD_1_START: PadButton(Vec2(0, 0), 0, height=3),
            pyxel.GAMEPAD_1_UP: PadButton(Vec2(0, 0), 0),
            pyxel.GAMEPAD_1_DOWN: PadButton(Vec2(0, 0), 0),
            pyxel.GAMEPAD_1_LEFT: PadButton(Vec2(0, 0), 0),
            pyxel.GAMEPAD_1_RIGHT: PadButton(Vec2(0, 0), 0),
        }

        GamePadImage.move(CONST.WINDOW.WIDTH // 2,
                          CONST.WINDOW.HEIGHT // 2 + 7)

        self.pad_pos = Vec2(GamePadImage.POS_X,
                            GamePadImage.POS_Y)

        x, y = self.pad_pos.x + 43, self.pad_pos.y
        self.buttons[pyxel.GAMEPAD_1_X].x = x
        self.buttons[pyxel.GAMEPAD_1_X].y = y - 10
        self.buttons[pyxel.GAMEPAD_1_A].x = x + 10
        self.buttons[pyxel.GAMEPAD_1_A].y = y
        self.buttons[pyxel.GAMEPAD_1_B].x = x
        self.buttons[pyxel.GAMEPAD_1_B].y = y + 10
        self.buttons[pyxel.GAMEPAD_1_Y].x = x - 10
        self.buttons[pyxel.GAMEPAD_1_Y].y = y

        x = self.pad_pos.x - 43
        self.buttons[pyxel.GAMEPAD_1_UP].x = x
        self.buttons[pyxel.GAMEPAD_1_UP].y = y - 10
        self.buttons[pyxel.GAMEPAD_1_RIGHT].x = x + 10
        self.buttons[pyxel.GAMEPAD_1_RIGHT].y = y
        self.buttons[pyxel.GAMEPAD_1_DOWN].x = x
        self.buttons[pyxel.GAMEPAD_1_DOWN].y = y + 10
        self.buttons[pyxel.GAMEPAD_1_LEFT].x = x - 10
        self.buttons[pyxel.GAMEPAD_1_LEFT].y = y

        x = self.pad_pos.x
        self.buttons[pyxel.GAMEPAD_1_SELECT].x = x - 10
        self.buttons[pyxel.GAMEPAD_1_SELECT].y = y
        self.buttons[pyxel.GAMEPAD_1_START].x = x + 10
        self.buttons[pyxel.GAMEPAD_1_START].y = y

        y = self.pad_pos.y - 27
        self.buttons[pyxel.GAMEPAD_1_LEFT_SHOULDER].x = x - 40
        self.buttons[pyxel.GAMEPAD_1_LEFT_SHOULDER].y = y
        self.buttons[pyxel.GAMEPAD_1_RIGHT_SHOULDER].x = x + 40
        self.buttons[pyxel.GAMEPAD_1_RIGHT_SHOULDER].y = y

        self.current_gamepad = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        for key_code, btn in self.buttons.items():
            if pyxel.btnp(key_code):
                btn.press()
            elif pyxel.btnr(key_code):
                btn.release()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.current_gamepad += 1
            # self.current_gamepad %= 2
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.current_gamepad -= 1
            # self.current_gamepad %= 2

    def draw_top_bar(self):
        pyxel.rect(0, 0, CONST.WINDOW.WIDTH, 14, CONST.COLOR.CREAM)
        pyxel.line(0, 15, CONST.WINDOW.WIDTH, 15, CONST.COLOR.BLACK)

        text_pos_x = CONST.WINDOW.WIDTH // 2 - 17
        text_pos_y = 5
        icon_size = 8

        pyxel.blt(text_pos_x - 8, text_pos_y - 2,
                  0,
                  136, 0,
                  icon_size, icon_size
                  )
        pyxel.blt(text_pos_x + 35, text_pos_y - 2,
                  0,
                  144, 0,
                  icon_size, icon_size
                  )
        pyxel.text(text_pos_x, text_pos_y,
                   f"GAMEPAD {self.current_gamepad+1}", CONST.COLOR.BLACK)

    def draw(self):
        pyxel.cls(2)

        self.draw_top_bar()

        pyxel.blt(
            GamePadImage.POS_X, GamePadImage.POS_Y - 41,
            0,
            0, 88,
            16, 16
        )
        GamePadImage.draw()

        for btn in self.buttons.values():
            btn.draw()

        btn_pos = self.buttons.get(pyxel.GAMEPAD_1_A).xy
        pyxel.text(btn_pos[0], btn_pos[1] - 2, "A", CONST.COLOR.BLACK)
        pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "A", CONST.COLOR.YELLOW)

        btn_pos = self.buttons.get(pyxel.GAMEPAD_1_B).xy
        pyxel.text(btn_pos[0], btn_pos[1] - 2, "B", CONST.COLOR.BLACK)
        pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "B", CONST.COLOR.YELLOW)

        btn_pos = self.buttons.get(pyxel.GAMEPAD_1_X).xy
        pyxel.text(btn_pos[0], btn_pos[1] - 2, "X", CONST.COLOR.BLACK)
        pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "X", CONST.COLOR.YELLOW)

        btn_pos = self.buttons.get(pyxel.GAMEPAD_1_Y).xy
        pyxel.text(btn_pos[0], btn_pos[1] - 2, "Y", CONST.COLOR.BLACK)
        pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "Y", CONST.COLOR.YELLOW)

        # btn_pos = self.buttons.get(pyxel.GAMEPAD_1_UP).xy
        # pyxel.text(btn_pos[0], btn_pos[1] - 2, "A", CONST.COLOR.BLACK)
        # pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "A", CONST.COLOR.YELLOW)

        # btn_pos = self.buttons.get(pyxel.GAMEPAD_1_RIGHT).xy
        # pyxel.text(btn_pos[0], btn_pos[1] - 2, "B", CONST.COLOR.BLACK)
        # pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "B", CONST.COLOR.YELLOW)

        # btn_pos = self.buttons.get(pyxel.GAMEPAD_1_DOWN).xy
        # pyxel.text(btn_pos[0], btn_pos[1] - 2, "X", CONST.COLOR.BLACK)
        # pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "X", CONST.COLOR.YELLOW)

        # btn_pos = self.buttons.get(pyxel.GAMEPAD_1_LEFT).xy
        # pyxel.text(btn_pos[0], btn_pos[1] - 2, "Y", CONST.COLOR.BLACK)
        # pyxel.text(btn_pos[0] - 1, btn_pos[1] - 2, "Y", CONST.COLOR.YELLOW)


if __name__ == "__main__":
    Window()
