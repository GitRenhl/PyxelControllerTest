import pyxel


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
            pyxel.GAMEPAD_1_A: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_B: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_DOWN: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_LEFT: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_LEFT_SHOULDER: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_RIGHT: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_RIGHT_SHOULDER: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_SELECT: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_START: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_UP: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_X: {"current": False, "ever": False},
            pyxel.GAMEPAD_1_Y: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_A: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_B: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_DOWN: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_LEFT: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_LEFT_SHOULDER: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_RIGHT: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_RIGHT_SHOULDER: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_SELECT: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_START: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_UP: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_X: {"current": False, "ever": False},
            pyxel.GAMEPAD_2_Y: {"current": False, "ever": False},
        }

        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btnp(pyxel.GAMEPAD_1_A):
            self.pressed_keys[pyxel.GAMEPAD_1_A]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_A]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_A):
            self.pressed_keys[pyxel.GAMEPAD_1_A]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_B):
            self.pressed_keys[pyxel.GAMEPAD_1_B]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_B]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_B):
            self.pressed_keys[pyxel.GAMEPAD_1_B]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_DOWN):
            self.pressed_keys[pyxel.GAMEPAD_1_DOWN]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_DOWN]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_DOWN):
            self.pressed_keys[pyxel.GAMEPAD_1_DOWN]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_LEFT):
            self.pressed_keys[pyxel.GAMEPAD_1_LEFT]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_LEFT]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_LEFT):
            self.pressed_keys[pyxel.GAMEPAD_1_LEFT]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_LEFT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_1_LEFT_SHOULDER]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_LEFT_SHOULDER]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_LEFT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_1_LEFT_SHOULDER]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_RIGHT):
            self.pressed_keys[pyxel.GAMEPAD_1_RIGHT]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_RIGHT]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_RIGHT):
            self.pressed_keys[pyxel.GAMEPAD_1_RIGHT]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_RIGHT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_1_RIGHT_SHOULDER]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_RIGHT_SHOULDER]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_RIGHT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_1_RIGHT_SHOULDER]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_SELECT):
            self.pressed_keys[pyxel.GAMEPAD_1_SELECT]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_SELECT]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_SELECT):
            self.pressed_keys[pyxel.GAMEPAD_1_SELECT]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_START):
            self.pressed_keys[pyxel.GAMEPAD_1_START]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_START]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_START):
            self.pressed_keys[pyxel.GAMEPAD_1_START]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_UP):
            self.pressed_keys[pyxel.GAMEPAD_1_UP]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_UP]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_UP):
            self.pressed_keys[pyxel.GAMEPAD_1_UP]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_X):
            self.pressed_keys[pyxel.GAMEPAD_1_X]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_X]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_X):
            self.pressed_keys[pyxel.GAMEPAD_1_X]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_1_Y):
            self.pressed_keys[pyxel.GAMEPAD_1_Y]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_1_Y]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_1_Y):
            self.pressed_keys[pyxel.GAMEPAD_1_Y]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_A):
            self.pressed_keys[pyxel.GAMEPAD_2_A]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_A]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_A):
            self.pressed_keys[pyxel.GAMEPAD_2_A]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_B):
            self.pressed_keys[pyxel.GAMEPAD_2_B]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_B]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_B):
            self.pressed_keys[pyxel.GAMEPAD_2_B]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_DOWN):
            self.pressed_keys[pyxel.GAMEPAD_2_DOWN]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_DOWN]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_DOWN):
            self.pressed_keys[pyxel.GAMEPAD_2_DOWN]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_LEFT):
            self.pressed_keys[pyxel.GAMEPAD_2_LEFT]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_LEFT]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_LEFT):
            self.pressed_keys[pyxel.GAMEPAD_2_LEFT]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_LEFT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_2_LEFT_SHOULDER]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_LEFT_SHOULDER]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_LEFT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_2_LEFT_SHOULDER]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_RIGHT):
            self.pressed_keys[pyxel.GAMEPAD_2_RIGHT]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_RIGHT]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_RIGHT):
            self.pressed_keys[pyxel.GAMEPAD_2_RIGHT]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_RIGHT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_2_RIGHT_SHOULDER]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_RIGHT_SHOULDER]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_RIGHT_SHOULDER):
            self.pressed_keys[pyxel.GAMEPAD_2_RIGHT_SHOULDER]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_SELECT):
            self.pressed_keys[pyxel.GAMEPAD_2_SELECT]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_SELECT]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_SELECT):
            self.pressed_keys[pyxel.GAMEPAD_2_SELECT]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_START):
            self.pressed_keys[pyxel.GAMEPAD_2_START]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_START]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_START):
            self.pressed_keys[pyxel.GAMEPAD_2_START]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_UP):
            self.pressed_keys[pyxel.GAMEPAD_2_UP]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_UP]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_UP):
            self.pressed_keys[pyxel.GAMEPAD_2_UP]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_X):
            self.pressed_keys[pyxel.GAMEPAD_2_X]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_X]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_X):
            self.pressed_keys[pyxel.GAMEPAD_2_X]["current"] = False

        if pyxel.btnp(pyxel.GAMEPAD_2_Y):
            self.pressed_keys[pyxel.GAMEPAD_2_Y]["current"] = True
            self.pressed_keys[pyxel.GAMEPAD_2_Y]["ever"] = True
        elif pyxel.btnr(pyxel.GAMEPAD_2_Y):
            self.pressed_keys[pyxel.GAMEPAD_2_Y]["current"] = False

    def draw(self):
        pyxel.cls(1)
        y = 0
        for k, v in self.pressed_keys.items():
            pyxel.text(60, y, self.keys_name[k], 7)

            if v.get("current"):
                col = 11
            else:
                col = 8

            pyxel.text(10, y, str(v['current']), col)

            if v.get("ever"):
                col = 11
            else:
                col = 8

            pyxel.text(35, y, str(v['ever']), col)

            y += 7


if __name__ == "__main__":
    Window()
