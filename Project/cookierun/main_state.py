from pico2d import *

import game_framework

from cookie import Cookie
from background import Background

name = "MainState"

cookie = None
background = None


def enter():
    global cookie, background
    cookie = Cookie()
    background = Background()


def exit():
    global cookie, background
    del cookie
    del background


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           game_framework.quit()
       else:
           cookie.handle_event(event)


def update():
    cookie.update()


def draw():
    clear_canvas()
    background.draw()
    cookie.draw()
    update_canvas()





