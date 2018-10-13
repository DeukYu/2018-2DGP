from pico2d import *

import game_framework

name = "main_lobby"

lobby = None
start = None


class Lobby:
    def __init__(self):
        self.image = load_image('main_lobby.png')

    def draw(self):
        self.image.draw(400, 300)


class Start_button:
    def __init__(self):
        self.image = load_image('start_button.png')

    def draw(self):
        self.image.draw(100, 100)


def enter():
    global lobby, start
    lobby = Lobby()
    start = Start_button()


def exit():
    global lobby, start
    del(lobby)
    del(start)


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           game_framework.quit()


def draw():
    clear_canvas()
    lobby.draw()
    start.draw()
    update_canvas()


def update():
    pass





