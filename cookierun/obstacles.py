from pico2d import *

import game_framework




class Jump:
    def __init__(self):
        self.x, self.y = 400, 115
        self.image_Jump_Obstacle = load_image('resource/obstacles/stage2/jump_obstacle.png')

    def enter(self):
        pass

    def update(self):
        self.x -= 10 * game_framework.frame_time

    def draw(self):
        self.image_Jump_Obstacle.clip_draw(0, 0, 104, 135, self.x, self.y, 104, 135)
