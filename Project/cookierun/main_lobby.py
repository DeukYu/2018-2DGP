from pico2d import *

import game_framework

name = "main_lobby"

imageLobby = None
imageStartButton = None
imageCookieButton = None
imagePetButton = None


class Lobby:
    def __init__(self):
        self.image = load_image('main_lobby.png')

    def draw(self):
        self.image.draw(400, 250)


class StartButton:
    SelectSB = 0

    def __init__(self):
            self.image = load_image('start_button.png')

    def draw(self):
        if SelectSB == 0:
            self.image.draw(600, 40)


class CookieSelectButton:
    def __init__(self):
        self.image = load_image('cookie_select.png')

    def draw(self):
        self.image.draw(615, 120)


class PetSelectButton:
    def __init__(self):
        self.image = load_image('pet_select.png')

    def draw(self):
        self.image.draw(625, 200)


def enter():
    global imageLobby, imageStartButton, imageCookieButton, imagePetButton
    imageLobby = Lobby()
    imageStartButton = StartButton()
    imageCookieButton = CookieSelectButton()
    pet = PetSelectButton()


def exit():
    global imageLobby, imageStartButton, imageCookieButton, imagePetButton
    del(imageLobby)
    del(imageStartButton)
    del(imageCookieButton)
    del(imagePetButton)


def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 500 - event.y - 1


x, y = 0, 0


def draw():
    clear_canvas()
    imageLobby.draw()
    imageStartButton.draw()
    imageCookieButton.draw()
    imagePetButton.draw()
    update_canvas()


def update():
    pass





