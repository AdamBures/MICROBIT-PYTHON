def on_forever():
    music.play_tone(622, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.play_tone(659, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.QUARTER))
    music.play_tone(622, music.beat(BeatFraction.QUARTER))
basic.forever(on_forever)

def on_in_background():
    basic.show_string("SHOOTING STARS")
control.in_background(on_in_background)
