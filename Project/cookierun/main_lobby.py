from pico2d import *

import game_framework

name = "main_lobby"

lobby = None
start = None
cookie = None
pet = None


class Lobby:
    def __init__(self):
        self.image = load_image('main_lobby.png')

    def draw(self):
        self.image.draw(400, 250)


class Start_button:
    def __init__(self):
        self.image = load_image('start_button.png')

    def draw(self):
        self.image.draw(600, 40)


class Cookie_selectbutton:
    def __init__(self):
        self.image = load_image('cookie_select.png')

    def draw(self):
        self.image.draw(615, 120)


class Pet_selectbutton:
    def __init__(self):
        self.image = load_image('pet_select.png')

    def draw(self):
        self.image.draw(625, 200)


def enter():
    global lobby, start, cookie, pet
    lobby = Lobby()
    start = Start_button()
    cookie = Cookie_selectbutton()
    pet = Pet_selectbutton()


def exit():
    global lobby, start, cookie, pet
    del(lobby)
    del(start)
    del(cookie)
    del(pet)


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
    cookie.draw()
    pet.draw()
    update_canvas()


def update():
    pass





