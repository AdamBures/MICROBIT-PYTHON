strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB_RGB)
strip2 = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
while True:
    x = input.acceleration(Dimension.X) / 2
    y = input.acceleration(Dimension.Y) / 2
    z = input.acceleration(Dimension.Z) / 2
    strip.shift(1)
    strip.set_pixel_color(0, neopixel.rgb(x, y, 0 - z))
    strip.show()
    strip2.shift(1)
    strip2.set_pixel_color(0, neopixel.rgb(x, y, 0 - z))
    strip2.show()
    basic.pause(100)

