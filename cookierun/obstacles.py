from pico2d import *

import game_framework
import game_world


class Obstacles:
    image = None

    def __init__(self, select=0):
        self.select = select
        self.x = 800
        if self.select == 0: # 점프
            self.image = load_image('resource/obstacles/stage2/jump_obstacle.png')
            self.y = 125
            self.Left_Right = 40
            self.Up_Down = 51

        elif self.select == 1: # 이중점프
            self.image = load_image('resource/obstacles/stage2/airjump_obstacle1.png')
            self.y = 155
            self.Left_Right = 40
            self.Up_Down = 82

        elif self.select == 2:
            self.image = load_image('resource/obstacles/stage2/airjump_obstacle2.png')
            self.y = 155
            self.Left_Right = 40
            self.Up_Down = 82

        elif self.select == 3:
            self.image = load_image('resource/obstacles/stage2/wing_obstacle1.png')
            self.y = 340
            self.Left_Right = 60
            self.Up_Down = 169

        elif self.select == 4:
            self.image = load_image('resource/obstacles/stage2/wing_obstacle2.png')
            self.y = 340
            self.Left_Right = 60
            self.Up_Down = 169

    def get_bb(self):
        return self.x - self.Left_Right, self.y - self.Up_Down, self.x + self.Left_Right, self.y + self.Up_Down

    def enter(self):
        pass

    def update(self):
        self.x -= 250 * game_framework.frame_time

        if self.x + self.Left_Right < 0:
            game_world.remove_object(self)

    def draw(self):
        if self.select == 0:
            self.image.clip_draw(0, 0, 80, 102, self.x, self.y, 80, 102)
            draw_rectangle(*self.get_bb())
        elif self.select == 1:
            self.image.clip_draw(0, 0, 80, 164, self.x, self.y, 80, 164)
            draw_rectangle(*self.get_bb())
        elif self.select == 2:
            self.image.clip_draw(0, 0, 80, 164, self.x, self.y, 80, 164)
            draw_rectangle(*self.get_bb())
        elif self.select == 3:
            self.image.clip_draw(0, 0, 120, 334, self.x, self.y, 120, 334)
            draw_rectangle(*self.get_bb())
        elif self.select == 4:
            self.image.clip_draw(0, 0, 120, 334, self.x, self.y, 120, 334)
            draw_rectangle(*self.get_bb())
