from pico2d import *

import game_framework

from cookie import Cookie

name = "MainState"

cookie = None
grass = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Pet:
    def __init__(self):
        self.x, self.y = 80, 100



def enter():
    global cookie, grass
    cookie = Cookie()
    grass = Grass()


def exit():
    global cookie, grass
    del(cookie)
    del(grass)


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
    #grass.draw()
    cookie.draw()
    update_canvas()





