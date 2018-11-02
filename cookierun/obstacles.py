from pico2d import *

import game_framework


class Obstacles:
    def __init__(self):
        self.image_Jump_Obstacle = load_image('resource/obstacles/stage2/jump_obstacle.png')
        self.image_Air1_Obstacle = load_image('resource/obstacles/stage2/airjump_obstacle1.png')
        self.image_Air2_Obstacle = load_image('resource/obstacles/stage2/airjump_obstacle2.png')
        self.image_Wing1_obstacle = load_image('resource/obstacles/stage2/wing_obstacle1.png')
        self.image_Wing2_obstacle = load_image('resource/obstacles/stage2/wing_obstacle2.png')

    def enter(self):
        pass

    def update(self):
        pass
        #self.x -= 10 * game_framework.frame_time

    def draw(self):
        self.image_Jump_Obstacle.clip_draw(0, 0, 80, 102, 300, 125, 80, 102)
        self.image_Air1_Obstacle.clip_draw(0, 0, 80, 164, 400, 155, 80, 164)
        self.image_Wing1_obstacle.clip_draw(0, 0, 80, 222, 600, 390, 80, 222)
