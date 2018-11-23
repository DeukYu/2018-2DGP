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
        self.image_coin = load_image('resource/gameinfo/cookie_Coin.png')
        self.image_jelly = load_image('resource/gameinfo/cookie_jelly.png')
        self.font = load_font('KL019.ttf', 36)

    def draw(self):
        self.image_HpBack.clip_draw(0, 0, (main_state.cookie.FullHp * 3), 26, (main_state.cookie.FullHp * 3) / 2 + 30, 450)
        self.image_HpFront.clip_draw(0, 0, (main_state.cookie.CurHp * 3), 26, (main_state.cookie.CurHp * 3) / 2 + 30, 450)
        self.image_HpEnd.draw((main_state.cookie.CurHp * 3) + 30, 450)
        self.image_HpStart.draw(30, 450)
        self.image_coin.draw(370, 480)
        self.font.draw(400, 480, '%d' % main_state.cookie.coin_cnt, (255, 255, 255))
        self.image_jelly.draw(700, 480)
        self.font.draw(720, 480, '%d' % main_state.cookie.jelly_cnt, (255, 255, 255))

    def update(self):
        pass
