from pico2d import *

import game_framework
import game_world


class Obstacles:
    def __init__(self, select=0):
        self.image_Jump_Obstacle = load_image('resource/obstacles/stage2/jump_obstacle.png')
        self.image_Air1_Obstacle = load_image('resource/obstacles/stage2/airjump_obstacle1.png')
        self.image_Air2_Obstacle = load_image('resource/obstacles/stage2/airjump_obstacle2.png')
        self.image_Wing1_obstacle = load_image('resource/obstacles/stage2/wing_obstacle1.png')
        self.image_Wing2_obstacle = load_image('resource/obstacles/stage2/wing_obstacle2.png')
        self.select = select
        self.x = 800
        if self.select == 0: # 점프
            self.y = 125
            self.Left_Right = 40
            self.Up_Down = 51
        elif self.select == 1 or self.select == 2: # 이중점프
            self.y = 155
            self.Left_Right = 40
            self.Up_Down = 82
        elif self.select == 3 or self.select == 4:
            self.y = 340
            self.Left_Right = 60
            self.Up_Down = 169

    def get_bb(self):
        return self.x - self.Left_Right, self.y - self.Up_Down, self.x + self.Left_Right, self.y + self.Up_Down

    def enter(self):
        pass

    def update(self):
        self.x -= 100 * game_framework.frame_time

    def draw(self):
        if self.select == 0:
            self.image_Jump_Obstacle.clip_draw(0, 0, 80, 102, self.x, self.y, 80, 102)
            draw_rectangle(*self.get_bb())
        elif self.select == 1:
            self.image_Air1_Obstacle.clip_draw(0, 0, 80, 164, self.x, self.y, 80, 164)
            draw_rectangle(*self.get_bb())
        elif self.select == 2:
            self.image_Air2_Obstacle.clip_draw(0, 0, 80, 164, self.x, self.y, 80, 164)
            draw_rectangle(*self.get_bb())
        elif self.select == 3:
            print(self.y)
            self.image_Wing1_obstacle.clip_draw(0, 0, 120, 334, self.x, self.y, 120, 334)
            draw_rectangle(*self.get_bb())
        elif self.select == 4:
            print(self.y)
            self.image_Wing2_obstacle.clip_draw(0, 0, 120, 334, self.x, self.y, 120, 334)
            draw_rectangle(*self.get_bb())
