def on_button_pressed_a():
    for i in range(5):
        led.plot(i, 0)
        basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for i in range(5):
        led.plot(i, i)
        basic.pause(100)
    
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for j in range(5):
        led.plot(0, j)
        basic.pause(100)
input.on_button_pressed(Button.B, on_button_pressed_b)
