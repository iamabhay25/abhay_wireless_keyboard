import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# =========================
# MATRIX CONFIG (YOUR EXACT PINS)
# =========================

keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3,
    board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13
)

keyboard.row_pins = (
    board.GP14, board.GP15, board.GP16,
    board.GP17, board.GP18, board.GP19
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# =========================
# KEYMAP (78-KEY WORKING LAYOUT)
# =========================

keyboard.keymap = [
    [
        # Row 0
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.NO,

        # Row 1
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.NO,

        # Row 2
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO,

        # Row 3
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.NO,

        # Row 4
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.SPC, KC.SPC, KC.RALT, KC.RGUI, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.NO, KC.NO,

        # Row 5 (unused row)
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

# =========================
# START KEYBOARD
# =========================

if __name__ == '__main__':
    keyboard.go()
