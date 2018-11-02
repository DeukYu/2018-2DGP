from pico2d import *

import cookie
import game_framework
import game_world
import random


class Items:
    image = None

    def __init__(self, select=0):
        self.select = select
        self.x = 800
        self.frame = 0
        if self.select == 0: # 젤리
            self.image = load_image('resource/items/Jelly.png')
            self.y = random.randint(125, 450)
            self.Left_Right = 12
            self.Up_Down = 16

        elif self.select == 1: # 실버 코인
            self.image = load_image('resource/items/Silver_Coin.png')
            self.y = random.randint(125, 450)
            self.Left_Right = 16
            self.Up_Down = 16

        elif self.select == 2:
            self.image = load_image('resource/items/Gold_Coin.png')
            self.y = random.randint(125, 450)
            self.Left_Right = 16
            self.Up_Down = 16

    def get_bb(self):
        return self.x - self.Left_Right, self.y - self.Up_Down, self.x + self.Left_Right, self.y + self.Up_Down

    def enter(self):
        pass

    def update(self):
        self.x -= 100 * game_framework.frame_time

        if self.select == 1 or self.select == 2:
            self.frame = (self.frame + cookie.FRAMES_PER_ACTION4 * cookie.ACTION_PER_TIME * game_framework.frame_time) % 4

        if self.x + self.Left_Right < 0:
            game_world.remove_object(self)

    def draw(self):
        if self.select == 0:
            self.image.clip_draw(self.frame * 0, 0, 24, 32, self.x, self.y, 24, 32)
            draw_rectangle(*self.get_bb())
        elif self.select == 1:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y, 32, 32)
            draw_rectangle(*self.get_bb())
        elif self.select == 2:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y, 32, 32)
            draw_rectangle(*self.get_bb())
