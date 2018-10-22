from pico2d import *

import game_framework

name = "MainState"

char = None
grass = None
font = None


class Font:
    def __init__(self):
        self.image = load_image('paused.png')

    def draw(self):
        self.image.draw(400, 300)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Character:
    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.image = load_image('cookie_run.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        delay(0.02)

    def draw(self):
        self.image.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)


class Pet:
    def __init__(self):
        self.x, self.y = 80, 100



def enter():
    global char, grass
    char = Character()
    grass = Grass()


def exit():
    global char, grass
    del(char)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()


def update():
    char.update()


def draw():
    clear_canvas()
    grass.draw()
    char.draw()
    update_canvas()





