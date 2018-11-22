import game_framework

import interface_state
from pico2d import *


name = "title_cookierun"
image = None
bgm = None

def enter():
    global image
    image = load_image('resource/title/title_cookieRun.png')

    global bgm
    bgm = load_music('resource/sound/bgm_main.ogg')
    bgm.set_volume(128)
    bgm.repeat_play()


def exit():
    global image
    del image

    global bgm
    del bgm


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(interface_state)

def draw():
    clear_canvas()
    image.draw(400, 250)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






