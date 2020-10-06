def check():
    if position_y > 2:
        led.unplot(position_x, 0)
        led.unplot(position_x, 1)

def tetromino_i():
    global position_y
    led.plot(position_x, position_y)
    basic.pause(100)
    position_y += 1
    check()
    led.plot(position_x, position_y)
    basic.pause(100)
    position_y += 1
    check()
    led.plot(position_x, position_y)
    basic.pause(100)
    position_y += 1
    check()
    led.plot(position_x, position_y)
    basic.pause(100)
    position_y += 1
    check()
    led.plot(position_x, position_y)


def on_button_pressed_ab():
    global lst2
    lst2 = ["i", "o", "t", "s", "z", "j"]
    random_number = randint(0, len(lst2))
    if lst2[0] == "i":
        tetromino_i()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

lst2: List[str] = ["i", "o", "t", "s", "z", "j"]
position_y = 0
position_x = 2
basic.show_string("TETRIS")

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
