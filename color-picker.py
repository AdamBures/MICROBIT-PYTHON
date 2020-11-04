def on_gesture_tilt_right():
    global G
    G += 16
    strip.show_color(neopixel.rgb(R, G, B))
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    global B
    B += -16
    strip.show_color(neopixel.rgb(R, G, B))
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_a():
    global R
    R += 16
    strip.show_color(neopixel.rgb(R, G, B))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global G
    G += -16
    strip.show_color(neopixel.rgb(R, G, B))
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_up():
    global B
    B += -16
    strip.show_color(neopixel.rgb(R, G, B))
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_b():
    global R
    R += -16
    strip.show_color(neopixel.rgb(R, G, B))
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_forever():
    global R,G,B
    if R+G+B == 765:
        R = 128
        G = 128
        B = 128
    elif R+G+B == 0:
        R = 128
        G = 128
        B = 128

basic.forever(on_forever)
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB_RGB)
R = 128
G = 128
B = 128
strip.show_color(neopixel.rgb(R, G, B))
