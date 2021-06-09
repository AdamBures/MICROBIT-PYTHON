def check():
    if position_y > 2:
        led.unplot(position_x, 0)
        led.unplot(position_x, 1)
def tetromino_i_laying():
    global position_y
    basic.clear_screen()
    for index in range(5):
        led.plot(0, position_y)
        led.plot(1, position_y)
        led.plot(2, position_y)
        led.plot(3, position_y)
        basic.pause(time)
        position_y += 1
        if index == 4:
            led.plot(0, position_y)
            led.plot(1, position_y)
            led.plot(2, position_y)
            led.plot(3, position_y)
        else:
            basic.clear_screen()

def on_gesture_logo_up():
    tetromino_i()
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_logo_down():
    tetromino_i_laying()
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def tetromino_i():
    global position_y
    basic.clear_screen()
    for index2 in range(5):
        led.plot(position_x, position_y)
        basic.pause(time)
        position_y += 1
        check()

def on_button_pressed_ab():
    global lst2, random_number
    lst2 = ["i", "o", "t", "s", "z", "j"]
    random_number = randint(0, len(lst2))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

random_number = 0
position_y = 0
position_x = 0
lst2: List[str] = []
time = 0
time = 500
lst2 = ["i", "o", "t", "s", "z", "j"]
position_x = 2
# basic.show_string("TETRIS")

def on_forever():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    basic.pause(400)
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
basic.forever(on_forever)
