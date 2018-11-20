import game_framework
import main_state
import game_world
import obstacles
import random
import items
import time

from pico2d import *


class HpBar:
    def __init__(self):
        self.image_Hp = load_image('resource/stage/cookie_Hp.png')
        self.image_HpBack = load_image('resource/stage/cookie_HpBack.png')
        self.image_HpEnd = load_image('resource/stage/cookie_Hpend.png')

    def draw(self):
        self.image_HpBack.clip_draw(0, 0, 500, 70, 240, 470)
        self.image_Hp.clip_draw(0, 0, 500, 70, 240, 470)
        self.image_HpEnd.draw_now(470, 470)

    def update(self):
        pass
