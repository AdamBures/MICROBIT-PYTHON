def on_button_pressed_a():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
