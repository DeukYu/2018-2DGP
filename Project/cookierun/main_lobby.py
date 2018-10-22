from pico2d import *

import game_framework
import main_state

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
    def __init__(self):
            self.image = load_image('start_button.png')
            self.motion = 0

    def draw(self):
            self.image.clip_draw(150 * self.motion, 0, 150, 50, 600, 40)


class CookieSelectButton:
    def __init__(self):
        self.image = load_image('cookie_select.png')
        self.motion = 0

    def draw(self):
        self.image.clip_draw(125 * self.motion, 0, 125, 50, 615, 120)


class PetSelectButton:
    def __init__(self):
        self.image = load_image('pet_select.png')
        self.motion = 0

    def draw(self):
        self.image.clip_draw(105 * self.motion, 0, 105, 50, 625, 200)


def enter():
    global imageLobby, imageStartButton, imageCookieButton, imagePetButton
    imageLobby = Lobby()
    imageStartButton = StartButton()
    imageCookieButton = CookieSelectButton()
    imagePetButton = PetSelectButton()


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
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 500 - event.y - 1
            if 600 - 75 <= x <= 600 + 75 and 40 - 25 <= y <= 40 + 25:
                imageStartButton.motion = 1
            else:
                imageStartButton.motion = 0
            if 625 - 55 <= x <= 625 + 55 and 200 - 25 <= y <= 200 + 25:
                imagePetButton.motion = 1
            else:
                imagePetButton.motion = 0
            if 615 - 120 <= x <= 615 + 120 and 120 - 25 <= y <= 120 + 25:
                imageCookieButton.motion = 1
            else:
                imageCookieButton.motion = 0
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if imageStartButton.motion == 1:
                game_framework.change_state(main_state)


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





