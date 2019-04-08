import pyxel


class STATE:
    CURRENT = 0
    EVER = 1


class Window:
    WIDTH = 200
    HEIGHT = 200

    def __init__(self):
        pyxel.init(self.WIDTH, self.HEIGHT, caption="Noise")
        pyxel.mouse(True)

        self.keys_name = {
            pyxel.GAMEPAD_1_A: "A",
            pyxel.GAMEPAD_1_B: "B",
            pyxel.GAMEPAD_1_DOWN: "DOWN",
            pyxel.GAMEPAD_1_LEFT: "LEFT",
            pyxel.GAMEPAD_1_LEFT_SHOULDER: "LEFT_SHOULDER",
            pyxel.GAMEPAD_1_RIGHT: "RIGHT",
            pyxel.GAMEPAD_1_RIGHT_SHOULDER: "RIGHT_SHOULDER",
            pyxel.GAMEPAD_1_SELECT: "SELECT",
            pyxel.GAMEPAD_1_START: "START",
            pyxel.GAMEPAD_1_UP: "UP",
            pyxel.GAMEPAD_1_X: "X",
            pyxel.GAMEPAD_1_Y: "Y",

            pyxel.GAMEPAD_2_A: "A",
            pyxel.GAMEPAD_2_B: "B",
            pyxel.GAMEPAD_2_DOWN: "DOWN",
            pyxel.GAMEPAD_2_LEFT: "LEFT",
            pyxel.GAMEPAD_2_LEFT_SHOULDER: "LEFT_SHOULDER",
            pyxel.GAMEPAD_2_RIGHT: "RIGHT",
            pyxel.GAMEPAD_2_RIGHT_SHOULDER: "RIGHT_SHOULDER",
            pyxel.GAMEPAD_2_SELECT: "SELECT",
            pyxel.GAMEPAD_2_START: "START",
            pyxel.GAMEPAD_2_UP: "UP",
            pyxel.GAMEPAD_2_X: "X",
            pyxel.GAMEPAD_2_Y: "Y",
        }

        self.pressed_keys = {
            pyxel.GAMEPAD_1_A: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_B: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_DOWN: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_LEFT: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_LEFT_SHOULDER: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_RIGHT: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_RIGHT_SHOULDER: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_SELECT: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_START: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_UP: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_X: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_1_Y: {STATE.CURRENT: False, STATE.EVER: False},

            pyxel.GAMEPAD_2_A: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_B: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_DOWN: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_LEFT: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_LEFT_SHOULDER: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_RIGHT: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_RIGHT_SHOULDER: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_SELECT: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_START: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_UP: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_X: {STATE.CURRENT: False, STATE.EVER: False},
            pyxel.GAMEPAD_2_Y: {STATE.CURRENT: False, STATE.EVER: False},
        }

        pyxel.run(self.update, self.draw)

    def update(self):
        for key in self.pressed_keys:
            if pyxel.btnp(key):
                self.pressed_keys[key][STATE.CURRENT] = True
                self.pressed_keys[key][STATE.EVER] = True
            elif pyxel.btnr(key):
                self.pressed_keys[key][STATE.CURRENT] = False

    def draw(self):
        pyxel.cls(1)
        y = 0
        for key, v in self.pressed_keys.items():
            pyxel.text(60, y, self.keys_name.get(key), 7)

            if v.get(STATE.CURRENT):
                col = 11
            else:
                col = 8

            pyxel.text(10, y, str(v.get(STATE.CURRENT)), col)

            if v.get(STATE.EVER):
                col = 11
            else:
                col = 8

            pyxel.text(35, y, str(v.get(STATE.EVER)), col)

            y += 7


if __name__ == "__main__":
    Window()
