strip: neopixel.Strip = None
num = 0

def on_button_pressed_a():
    global strip, num
    music.start_melody(music.built_in_melody(Melodies.BIRTHDAY), MelodyOptions.ONCE)
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
    while True:
        if num == 24:
            num = 0
        x = randint(1, 256)
        y = randint(1, 256)
        z = randint(1, 256)
        strip.set_pixel_color(num, neopixel.rgb(x, y, z))
        strip.show()
        basic.pause(100)
        num += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global strip, num
    value: List[number] = []
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
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
    while True:
        if num == 24:
            num = 0
        x2 = randint(1, 256)
        y2 = randint(1, 256)
        z2 = randint(1, 256)
        strip.set_pixel_color(num, neopixel.rgb(x2, y2, z2))
        strip.show()
        basic.pause(100)
        num += 1
input.on_button_pressed(Button.B, on_button_pressed_b)
