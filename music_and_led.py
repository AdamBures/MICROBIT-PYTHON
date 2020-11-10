def on_button_pressed_a():
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
    music.play_tone(330, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    basic.pause(100)
    music.play_tone(330, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    basic.pause(100)
    music.play_tone(440, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    basic.pause(100)
    music.play_tone(294, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
    music.play_tone(294, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    basic.pause(100)
    music.play_tone(392, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
    strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(100)
    music.play_tone(349, music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global song
    song = [[622, 120],
        [554, 120],
        [523, 120],
        [554, 120],
        [659, 240],
        [0, 240],
        [740, 120],
        [659, 120],
        [622, 120],
        [659, 120],
        [830, 240],
        [0, 240],
        [880, 120],
        [830, 120],
        [784, 120],
        [830, 120],
        [1244, 120],
        [1108, 120],
        [1046, 120],
        [1108, 120],
        [1244, 120],
        [1108, 120],
        [1046, 120],
        [1108, 120],
        [1318, 480],
        [1108, 240],
        [1318, 240],
        [987, 60],
        [1108, 60],
        [1244, 120],
        [1108, 240],
        [987, 240],
        [1108, 240],
        [987, 60],
        [1108, 60],
        [1244, 120],
        [1108, 240],
        [987, 240],
        [1108, 240],
        [987, 60],
        [1108, 60],
        [1244, 120],
        [1108, 240],
        [987, 240],
        [932, 240],
        [830, 480],
        [622, 120],
        [554, 60],
        [523, 120],
        [554, 120],
        [659, 240],
        [0, 240],
        [740, 120],
        [659, 120],
        [622, 120],
        [659, 120],
        [830, 240],
        [0, 240],
        [880, 120],
        [830, 120],
        [784, 120],
        [830, 120],
        [1244, 120],
        [1108, 120],
        [1046, 120],
        [1108, 120],
        [1244, 120],
        [1108, 120],
        [1046, 120],
        [1108, 120],
        [1318, 480],
        [1108, 240],
        [1318, 240],
        [987, 60],
        [1108, 60],
        [1244, 120],
        [1108, 240],
        [987, 240],
        [1108, 240],
        [987, 60],
        [1108, 60],
        [1244, 120],
        [1108, 240],
        [987, 240],
        [1108, 240],
        [987, 60],
        [1108, 60],
        [1244, 120],
        [1108, 240],
        [987, 240],
        [932, 240],
        [830, 480]]
    for value2 in song:
        music.play_tone(value2[0], value2[1])
        lst = ["indigo", "red", "yellow", "green", "black", "white"]
        x = randint(0, len(lst))
        if x == 0:
            strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
        elif x == 1:
            strip.show_color(neopixel.colors(NeoPixelColors.RED))
        elif x == 2:
            strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        elif x == 3:
            strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        elif x == 4:
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        elif x == 5:
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
input.on_button_pressed(Button.B, on_button_pressed_b)

song: List[List[number]] = []
strip: neopixel.Strip = None
value: List[number] = []
num = 0
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
strip.set_brightness(255)
