def on_button_pressed_a():
    for i in range(5):
        led.plot(i, 0)
        basic.pause(100)
        led.plot(i, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for j in range(5):
        led.plot(j, j)
        basic.pause(100)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for k in range(5):
        led.plot(0, k)
        basic.pause(100)
        led.plot(4,k)
input.on_button_pressed(Button.B, on_button_pressed_b)
