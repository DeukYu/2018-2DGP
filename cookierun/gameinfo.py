import game_framework
import main_state
import game_world
import obstacles
import cookie
import random
import items
import time

from pico2d import *


class GameInfo:
    def __init__(self):
        self.image_HpFront = load_image('resource/gameinfo/cookie_HpFront.png')
        self.image_HpBack = load_image('resource/gameinfo/cookie_HpBack.png')
        self.image_HpStart = load_image('resource/gameinfo/cookie_HpStart.png')
        self.image_HpEnd = load_image('resource/gameinfo/cookie_HpEnd.png')

    def draw(self):
        self.image_HpBack.clip_draw(0, 0, 500, 70, 260, 450)
        self.image_HpFront.clip_draw(0, 0, 500, 70, 260, 450)
        self.image_HpEnd.draw(490, 450)
        self.image_HpStart.draw(260, 450, 500, 70)

    def update(self):
        pass
