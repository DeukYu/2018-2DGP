from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
bottom = 1
dir = 0

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, bottom * 100, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    if dir == 0:
        x += 10
        if x >= 800:
            dir = 1
            bottom = 0
    elif dir == 1:
        x -= 10
        if x <= 0:
            dir = 0
            bottom = 1
    delay(0.03)
    get_events()

close_canvas()
