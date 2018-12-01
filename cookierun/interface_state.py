from pico2d import *

import os

import game_framework
import main_state

name = "interface_state"

imageBackground = None
imageStartButton = None
imageCookieButton = None
imagePetButton = None
imageCookieSelection = None
imageShowCookie = None
imageShowPet = None
imagePetSelection = None
imageSelectButton = None
bgmLobby = None
button_sound = None


class ButtonSound:
    def __init__(self):
        self.on_sound = load_wav('resource/sound/SFX_Button_On.wav')
        self.on_sound.set_volume(32)
        self.off_sound = load_wav('resource/sound/SFX_Button_Off.wav')
        self.off_sound.set_volume(32)

    def button_on(self):
        self.on_sound.play()

    def button_off(self):
        self.off_sound.play()


class Background:
    def __init__(self):
        self.image = load_image('resource/interface/interface_background.png')

    def draw(self):
        self.image.draw(400, 250)


class StartButton:
    def __init__(self):
            self.image = load_image('resource/interface/interface_startbutton.png')
            self.motion = 0

    def draw(self):
            self.image.clip_draw(150 * self.motion, 0, 150, 50, 600, 40)


class CookieSelectButton:
    def __init__(self):
        self.image = load_image('resource/interface/interface_cookieselectbutton.png')
        self.motion = 0

    def draw(self):
        self.image.clip_draw(125 * self.motion, 0, 125, 50, 615, 120)


class CookieSelectWindow:
    def __init__(self):
        self.image = load_image('resource/interface/interface_cookieselect.png')
        self.imageExit = load_image('resource/interface/interface_exit.png')
        self.ExitMotion = 0
        self.Exit = 0

    def draw(self):
        if Click == 2:
            self.image.draw(400, 250)
            if self.ExitMotion == 1:
                self.imageExit.draw(585, 335)


class PetSelectButton:
    def __init__(self):
        self.image = load_image('resource/interface/interface_petselectbutton.png')
        self.motion = 0

    def draw(self):
        self.image.clip_draw(105 * self.motion, 0, 105, 50, 625, 200)


class PetSelectWindow:
    def __init__(self):
        self.image = load_image('resource/interface/interface_petselect.png')
        self.imageExit = load_image('resource/interface/interface_exit.png')
        self.ExitMotion = 0
        self.Exit = 0

    def draw(self):
        if Click == 1:
            self.image.draw(400, 250)
            if self.ExitMotion == 1:
                self.imageExit.draw(585, 335)


class SelectButton:
    def __init__(self):
        self.image = load_image('resource/interface/interface_selectbutton.png')
        self.motion = 0
    def draw(self):
        if self.motion == 1:
            self.image.draw(252.5, 171)
        elif self.motion == 2:
            self.image.draw(351, 171)
        elif self.motion == 3:
            self.image.draw(449, 171)
        elif self.motion == 4:
            self.image.draw(550, 171)

class ShowCookie:
    def __init__(self):
        self.image = load_image('resource/interface/interface_character.png')

    def draw(self):
            self.image.clip_draw(150 * CharChoice, 0, 150, 150, 150, 100)


class ShowPet:
    def __init__(self):
        self.image = load_image('resource/interface/interface_pet.png')

    def draw(self):
        self.image.clip_draw(80 * PetChoice, 0, 80, 80, 60, 100)


class Bgm:
    def __init__(self):
        self.bgm = load_music('resource/sound/bgm_lobby.ogg')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


def enter():
    global imageBackground, imageStartButton, imageCookieButton, imagePetButton, imageCookieSelection, imageShowCookie
    global imagePetSelection, imageShowPet, imageSelectButton
    imageBackground = Background()
    imageStartButton = StartButton()
    imageCookieButton = CookieSelectButton()
    imagePetButton = PetSelectButton()
    imageCookieSelection = CookieSelectWindow()
    imageShowCookie = ShowCookie()
    imageShowPet = ShowPet()
    imagePetSelection = PetSelectWindow()
    imageSelectButton = SelectButton()

    global bgmLobby
    bgmLobby = Bgm()

    global button_sound
    button_sound = ButtonSound()


def exit():
    global imageBackground, imageStartButton, imageCookieButton, imagePetButton, imageCookieSelection, imageShowCookie
    global imagePetSelection, imageShowPet, imageSelectButton
    del imageBackground
    del imageStartButton
    del imageCookieButton
    del imagePetButton
    del imageCookieSelection
    del imageShowCookie
    del imageShowPet
    del imagePetSelection
    del imageSelectButton

    global bgmLobby
    del bgmLobby

    global button_sound
    del button_sound

def handle_events():
    global x, y, Click, CharChoice, PetChoice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 500 - event.y - 1
            if Click == 0: #Lobby
                if 600 - 75 <= x <= 600 + 75 and 40 - 25 <= y <= 40 + 25:
                    imageStartButton.motion = 1
                    button_sound.button_on()
                else:
                    imageStartButton.motion = 0
                if 625 - 55 <= x <= 625 + 55 and 200 - 25 <= y <= 200 + 25:
                    imagePetButton.motion = 1
                    button_sound.button_on()
                else:
                    imagePetButton.motion = 0
                if 615 - 60 <= x <= 615 + 60 and 120 - 25 <= y <= 120 + 25:
                    imageCookieButton.motion = 1
                    button_sound.button_on()
                else:
                    imageCookieButton.motion = 0
            elif Click == 1: # Pet
                if 600 - 25 <= x <= 600 - 5 and 350 - 25 <= y <= 350 - 5:
                    imagePetSelection.Exit = 1
                    imagePetSelection.ExitMotion = 1
                    button_sound.button_on()
                elif 150 + 10 <= y <= 150 + 33:
                    if 200 + 15 <= x <= 200 + 90:
                        PetChoice = 0
                        imagePetSelection.Exit = 1
                        imageSelectButton.motion = 1
                    elif 200 + 113 <= x <= 200 + 188:
                        PetChoice = 1
                        imagePetSelection.Exit = 1
                        imageSelectButton.motion = 2
                    elif 200 + 211 <= x <= 200 + 286:
                        PetChoice = 2
                        imagePetSelection.Exit = 1
                        imageSelectButton.motion = 3
                    elif 200 + 310 <= x <= 200 + 385:
                        PetChoice = 3
                        imagePetSelection.Exit = 1
                        imageSelectButton.motion = 4
                    button_sound.button_on()
                else:
                    imagePetSelection.Exit = 0
                    imagePetSelection.ExitMotion = 0
                    imageSelectButton.motion = 0
            elif Click == 2: # Cookie
                if 600 - 25 <= x <= 600 - 5 and 350 - 25 <= y <= 350 - 5:
                    imageCookieSelection.Exit = 1
                    imageCookieSelection.ExitMotion = 1
                    button_sound.button_on()
                elif 150 + 10 <= y <= 150 + 33:
                    if 200 + 15 <= x <= 200 + 90:
                        CharChoice = 0
                        imageCookieSelection.Exit = 1
                        imageSelectButton.motion = 1
                    elif 200 + 113 <= x <= 200 + 188:
                        CharChoice = 1
                        imageCookieSelection.Exit = 1
                        imageSelectButton.motion = 2
                    elif 200 + 211 <= x <= 200 + 286:
                        CharChoice = 2
                        imageSelectButton.motion = 3
                        imageCookieSelection.Exit = 1
                    elif 200 + 310 <= x <= 200 + 385:
                        CharChoice = 3
                        imageCookieSelection.Exit = 1
                        imageSelectButton.motion = 4
                    button_sound.button_on()
                else:
                    imageCookieSelection.Exit = 0
                    imageCookieSelection.ExitMotion = 0
                    imageSelectButton.motion = 0
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if Click == 0:
                if imagePetButton.motion == 1:
                    Click = 1
                elif imageCookieButton.motion == 1:
                    Click = 2
                elif imageStartButton.motion == 1:
                    game_framework.change_state(main_state)
            elif Click == 1:
                if imagePetSelection.Exit == 1:
                    Click = 0
                    imagePetSelection.Exit = 0
                    imageSelectButton.motion = 0
            elif Click == 2:
                if imageCookieSelection.Exit == 1:
                    Click = 0
                    imageCookieSelection.Exit = 0
                    imageSelectButton.motion = 0


x, y = 0, 0

Click, CharChoice, PetChoice = 0, 0, 0


def draw():
    clear_canvas()
    imageBackground.draw()
    imageStartButton.draw()
    imageCookieButton.draw()
    imagePetButton.draw()
    imageShowCookie.draw()
    imageShowPet.draw()
    imageCookieSelection.draw()
    imagePetSelection.draw()
    imageSelectButton.draw()
    update_canvas()


def update():
    pass





