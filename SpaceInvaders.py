"""
TODO:
 ADD TIME CONSTANT
 LOADING MENU
 TEXT
 Resetting level and ending game
"""


def second_level():
    first_level()


def on_button_pressed_a():
    lod.move(-1)


input.on_button_pressed(Button.A, on_button_pressed_a)


def first_level():
    global lod, nepritel1, nepritel2, nepritel3, nepritel4, nepritel5
    lod = game.create_sprite(2, 4)
    basic.pause(200)
    nepritel1 = game.create_sprite(0, 0)
    basic.pause(200)
    nepritel2 = game.create_sprite(1, 1)
    basic.pause(200)
    nepritel3 = game.create_sprite(2, 0)
    basic.pause(200)
    nepritel4 = game.create_sprite(3, 1)
    basic.pause(200)
    nepritel5 = game.create_sprite(4, 0)


def on_button_pressed_ab():
    global strela, hitbox, hitbox2, level, score
    strela = game.create_sprite(lod.get(LedSpriteProperty.X), lod.get(LedSpriteProperty.Y))
    hitbox = game.create_sprite(1, 0)
    hitbox2 = game.create_sprite(3, 0)
    strela.change(LedSpriteProperty.BRIGHTNESS, 80)
    hitbox.set(LedSpriteProperty.BRIGHTNESS, 0)
    hitbox2.set(LedSpriteProperty.BRIGHTNESS, 0)
    for index in range(4):
        strela.change(LedSpriteProperty.Y, -1)
        basic.pause(200)
    if strela.is_touching(nepritel1):
        nepritel1.delete()
        score += 100
    elif strela.is_touching(hitbox):
        nepritel2.delete()
        hitbox.delete()
        score += 100
    elif strela.is_touching(nepritel3):
        nepritel3.delete()
        score += 100
    elif strela.is_touching(hitbox2):
        nepritel4.delete()
        hitbox2.delete()
        score += 100
    elif strela.is_touching(nepritel5):
        nepritel5.delete()
        score += 100
    strela.delete()
    if nepritel1.is_deleted() and nepritel2.is_deleted() and nepritel3.is_deleted() \
            and nepritel4.is_deleted() and nepritel5.is_deleted():
        lod.delete()
        basic.show_string("" + str(level))
        level = level + 1
        second_level()


input.on_button_pressed(Button.AB, on_button_pressed_ab)


def on_button_pressed_b():
    lod.move(1)


input.on_button_pressed(Button.B, on_button_pressed_b)

score = 0
enemy_strela: game.LedSprite = None
hitbox2: game.LedSprite = None
hitbox: game.LedSprite = None
strela: game.LedSprite = None
nepritel5: game.LedSprite = None
nepritel4: game.LedSprite = None
nepritel3: game.LedSprite = None
nepritel2: game.LedSprite = None
nepritel1: game.LedSprite = None
lod: game.LedSprite = None
enemy_strela2 = None
level = 1
lod = game.create_sprite(2, 4)
basic.pause(200)
nepritel1 = game.create_sprite(0, 0)
basic.pause(200)
nepritel2 = game.create_sprite(1, 1)
basic.pause(200)
nepritel3 = game.create_sprite(2, 0)
basic.pause(200)
nepritel4 = game.create_sprite(3, 1)
basic.pause(200)
nepritel5 = game.create_sprite(4, 0)
TIME = 500
SPEED = 0.5


def on_forever():
    global enemy_strela
    enemy_strela = game.create_sprite(randint(0, 4), 0)
    enemy_strela.change(LedSpriteProperty.BRIGHTNESS, 150)
    basic.pause(100)
    enemy_strela.turn(Direction.RIGHT, 90)
    for index2 in range(4):
        enemy_strela.move(1)
        basic.pause(TIME//SPEED)
    if enemy_strela.is_touching(lod):
        basic.show_string("GAME OVER!")
        basic.show_string(str(score))
    enemy_strela.delete()


basic.forever(on_forever)