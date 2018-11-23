from pico2d import *

import cookie
import game_framework
import game_world
import main_state
import random
import obstacles


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

        elif self.select == 3:
            self.image = load_image('resource/items/Power_Up.png')
            self.y = 250
            self.Left_Right = 25
            self.Up_Down = 25

        elif self.select == 4:
            self.image = load_image('resource/items/Hp_Up.png')
            self.y = 250
            self.Left_Right = 25
            self.Up_Down = 25

    def get_bb(self):
        return self.x - self.Left_Right, self.y - self.Up_Down, self.x + self.Left_Right, self.y + self.Up_Down

    def enter(self):
        pass

    def update(self):
        self.x -= 250 * game_framework.frame_time

        if self.select == 1 or self.select == 2 or self.select == 3 or self.select == 4:
            self.frame = (self.frame + cookie.FRAMES_PER_ACTION4 * cookie.ACTION_PER_TIME1 * game_framework.frame_time) % 4

        if self.x + self.Left_Right < 0:
            game_world.remove_object(self)
        elif main_state.collide(self, main_state.cookie):
            if self.select == 0:
                main_state.cookie.jelly_cnt += 1
            elif self.select == 1:
                main_state.cookie.coin_cnt += 1
            elif self.select == 2:
                main_state.cookie.coin_cnt += 2
            elif self.select == 3:
                pass
            elif self.select == 4:
                main_state.cookie.CurHp += 30
                if main_state.cookie.CurHp > main_state.cookie.FullHp:
                    main_state.cookie.CurHp = main_state.cookie.FullHp
            game_world.remove_object(self)

    def draw(self):
        if self.select == 0: # 젤리
            self.image.clip_draw(self.frame * 0, 0, 24, 32, self.x, self.y, 24, 32)
            draw_rectangle(*self.get_bb())
        elif self.select == 1 or self.select == 2:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y, 32, 32)
            draw_rectangle(*self.get_bb())
        elif self.select == 3 or self.select == 4:
            self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y, 50, 50)
            draw_rectangle(*self.get_bb())
