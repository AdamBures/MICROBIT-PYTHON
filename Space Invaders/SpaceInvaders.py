def on_button_pressed_a():
    ship.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)


def first_level():
    global ship, enemy1, enemy2, enemy3, enemy4, enemy5
    ship = game.create_sprite(2, 4)
    basic.pause(200)
    enemy1 = game.create_sprite(0, 0)
    basic.pause(200)
    enemy2 = game.create_sprite(1, 1)
    basic.pause(200)
    enemy3 = game.create_sprite(2, 0)
    basic.pause(200)
    enemy4 = game.create_sprite(3, 1)
    basic.pause(200)
    enemy5 = game.create_sprite(4, 0)


def on_button_pressed_ab():
    global shoot, hitbox, hitbox2, SCORE, LEVEL, SPEED
    shoot = game.create_sprite(ship.get(LedSpriteProperty.X), ship.get(LedSpriteProperty.Y))
    hitbox = game.create_sprite(1, 0)
    hitbox2 = game.create_sprite(3, 0)
    shoot.change(LedSpriteProperty.BRIGHTNESS, 80)
    hitbox.set(LedSpriteProperty.BRIGHTNESS, 0)
    hitbox2.set(LedSpriteProperty.BRIGHTNESS, 0)
    for index in range(4):
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(200)
    if shoot.is_touching(enemy1):
        enemy1.delete()
        SCORE += 100
    elif shoot.is_touching(hitbox):
        enemy2.delete()
        hitbox.delete()
        SCORE += 100
    elif shoot.is_touching(enemy3):
        enemy3.delete()
        SCORE += 100
    elif shoot.is_touching(hitbox2):
        enemy4.delete()
        hitbox2.delete()
        SCORE += 100
    elif shoot.is_touching(enemy5):
        enemy5.delete()
        SCORE += 100
    shoot.delete()
    if enemy1.is_deleted() and enemy2.is_deleted() and enemy3.is_deleted() \
            and enemy4.is_deleted() and enemy5.is_deleted():
        ship.delete()
        LEVEL += 1
        SPEED += 0.5
        basic.show_string("" + str(LEVEL))
        first_level()
input.on_button_pressed(Button.AB, on_button_pressed_ab)


def on_button_pressed_b():
    ship.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

SCORE = 0
hitbox2: game.LedSprite = None
hitbox: game.LedSprite = None
shoot: game.LedSprite = None
LEVEL = 0
nepritel: List[number] = []
nepritel6 = None
enemy_shoot: game.LedSprite = None
enemy_shoot2 = None
music.start_meshipy(music.built_in_meshipy(Meshipies.RINGTONE), MeshipyOptions.ONCE)
basic.pause(100)
basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)

basic.pause(100)
basic.show_icon(IconNames.SMALL_SQUARE)
basic.pause(100)
basic.show_icon(IconNames.SQUARE)
ship = game.create_sprite(2, 4)
basic.pause(200)
enemy1 = game.create_sprite(0, 0)
basic.pause(200)
enemy2 = game.create_sprite(1, 1)
basic.pause(200)
enemy3 = game.create_sprite(2, 0)
basic.pause(200)
enemy4 = game.create_sprite(3, 1)
basic.pause(200)
enemy5 = game.create_sprite(4, 0)
TIME = 500
SPEED = 1


def on_forever():
    global enemy_shoot, LEVEL, SCORE
    if LEVEL != 0:
        enemy_shoot = game.create_sprite(randint(0, 4), 0)
        enemy_shoot.change(LedSpriteProperty.BRIGHTNESS, 150)
        basic.pause(100)
        enemy_shoot.turn(Direction.RIGHT, 90)
        for index2 in range(4):
            enemy_shoot.move(1)
            basic.pause(Math.idiv(TIME, SPEED))
        if enemy_shoot.is_touching(ship):
            basic.clear_screen()
            basic.show_string("GAME OVER! " + str(SCORE))
            basic.clear_screen()
            SCORE = 0
            LEVEL = 0
        enemy_shoot.delete()
basic.forever(on_forever)
