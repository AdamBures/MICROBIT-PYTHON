tries = 0
score = 0
number = randint(0, 10)

def on_button_pressed_a():
    global score
    score += 1
    if score > 10:
        score = 0
        basic.show_number(score)
    basic.show_number(score)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_down():
    global score, number
    score = 0
    number = 0
    basic.show_string("Reset")
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_ab():
    global tries
    while tries < 3:
        if score == number:
            basic.show_string(f"You have found the number. It took only {tries}. ")
        elif score >= number:
            basic.show_string(f"The number is smaller. You have {tries} left")
            tries += 1
            return on_button_pressed_a()
        else:
            basic.show_string(f"The number is bigger. You have {tries} left")
            tries += 1
            return on_button_pressed_a()
    basic.show_string("You've lost :(")
    return on_gesture_logo_down()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global score
    if score > 0:
        score = score - 1
        basic.show_number(score)
    else:
        return on_button_pressed_a()
input.on_button_pressed(Button.B, on_button_pressed_b)
