def on_button_pressed_a():
    basic.show_leds("""
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # . . . .
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        # . . . .
        # # . . .
        # . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        # # . . .
        # . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # # .
        . . . . .
        # . . . .
        # # . . .
        # . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . # .
        . . . # .
        # . # # .
        # # . . .
        # . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . # .
        # . . # .
        # # # # .
        # . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . # .
        # # . # .
        # . # # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # . .
        . . . . .
        # . . # .
        # # . # .
        # . # # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
        . # # . .
        # . # # .
        # # . # .
        # . # # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . # . . .
        # # # # .
        # # # # .
        # . # # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # # .
        . # . . .
        # # # # .
        # # # # .
        # . # # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # . .
        . # # # .
        # # # # .
        # # # # .
        # . # # .
        """)
    basic.pause(100)
    basic.clear_screen()
    basic.show_string("Konec hry!")
    basic.clear_screen()
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.A, on_button_pressed_a)
