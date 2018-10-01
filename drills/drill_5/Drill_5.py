from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def pos_1():
    x, y, frame_x, frame_y = 203, 535, 0, 0
    while x > 132 and y > 243:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100,100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x -= (203 - 132) / 100
        y -= (535 - 243) / 100
        delay(0.03)
def pos_2():
    x, y, frame_x, frame_y = 132, 243, 0, 1
    while x < 535 and y < 470:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x += (535 - 132) / 100
        y += (470 - 243) / 100
        delay(0.03)

def pos_3():
    x, y, frame_x, frame_y = 535, 470, 0, 1
    while x < 715 and y > 136:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x += (715 - 535) / 100
        y -= (470 - 136) / 100
        delay(0.03)

def pos_4():
    x, y, frame_x, frame_y = 715, 136, 0, 0
    while x > 316 and y < 225:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x -= (715 - 316) / 100
        y += (225 - 136) / 100
        delay(0.03)
    pass
def pos_5():
    x, y, frame_x, frame_y = 316, 225, 0, 1
    while x < 510 and y > 92:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x += (510 - 316) / 100
        y -= (225 - 92) / 100
        delay(0.03)

def pos_6():
    x, y, frame_x, frame_y = 510, 92, 0, 1
    while x < 692 and y < 518:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x += (692 - 510) / 100
        y += (518 - 92) / 100
        delay(0.03)

def pos_7():
    x, y, frame_x, frame_y = 692, 518, 0, 0
    while x > 682 and y > 336:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x -= (692 - 682) / 100
        y -= (518 - 336) / 100
        delay(0.03)

def pos_8():
    x, y, frame_x, frame_y = 682, 336, 0, 1
    while x < 712 and y < 349:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x += (712 - 682) / 100
        y += (349 - 336) / 100
        delay(0.03)
    pass
def pos_9():
    x, y, frame_x, frame_y = 682, 336, 0, 1
    while x < 712 and y < 349:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x += (712 - 682) / 100
        y += (349 - 336) / 100
        delay(0.03)
    pass
def pos_10():
    pass

while True:
    #pos_1()
    #pos_2()
    #pos_3()
    #pos_4()
    #pos_5()
    #pos_6()
    #pos_7()
    #pos_8()

#running = True
#
#char_x = 203
#char_y = 535
#
#frame_x = 0
#frame_y = 1
#dir_x = 0
#dir_y = 0
#i = 1
#bmove_x = True
#bmove_y = True
#
#
#def handle_events():
#    # fill here
#    global running
#    events = get_events()
#    for event in events:
#        if event.type == SDL_QUIT:
#            running = False
#        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#            running = False
#
#
#x = [203, 132, 535, 477, 715, 316, 510, 692, 682, 712]
#y = [535, 243, 470, 203, 136, 225, 92, 518, 336, 349]
#
#while running:
#    clear_canvas()
#    grass.draw(400, 30)
#    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, char_x, char_y)
#    update_canvas()
#
#    handle_events()
#    frame_x = (frame_x + 1) % 8
#
#    if char_x < x[i]:
#        frame_y = 1
#        dir_x = 1
#    elif char_x > x[i]:
#        frame_y = 0
#        dir_x = -1
#    if char_y < y[i]:
#        dir_y = 1
#    elif char_y > y[i]:
#        dir_y = -1
#    if x[i] - 5 < char_x < x[i] + 5 and y[i] - 5 < char_y < y[i] + 5:
#        if i == 9:
#            i = 0
#        else:
#            i += 1
#        bmove_x = True
#        bmove_y = True
#    elif x[i] - 5 < char_x < x[i] + 5:
#        bmove_x = False
#    elif y[i] - 5 < char_y < y[i] + 5:
#        bmove_y = False
#
#    if bmove_x == True:
#        char_x += dir_x * 5
#    if bmove_y == True:
#        char_y += dir_y * 5
#    delay(0.03)
#
#close_canvas()
#
#
#
#
#
#
