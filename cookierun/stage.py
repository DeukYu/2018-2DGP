import game_framework
from pico2d import *


class Stage:
    def __init__(self):
        self.imageGround = load_image('resource/stage/First_ground.png')
        self.imageFrontGround = load_image('resource/stage/First_Frontground.png')
        self.imageBackGround = load_image('resource/stage/First_Background.png')
        self.Gx1 = 400
        self.Gx2 = 1200
        self.Fx = 800
        self.Bx1 = 400
        self.Bx2 = 1200

    def draw(self):
        self.imageBackGround.clip_draw(0, 0, 800, 500, self.Gx1, 250, 800, 500)
        self.imageBackGround.clip_draw(0, 0, 800, 500, self.Gx2, 250, 800, 500)
        self.imageFrontGround.clip_draw(0, 0, 1600, 500, self.Fx, 250, 1600, 500)
        self.imageGround.clip_draw(0, 0, 800, 500, self.Bx1, 250, 800, 500)
        self.imageGround.clip_draw(0, 0, 800, 500, self.Bx2, 250, 800, 500)

    def update(self):
        self.Gx1 -= 100 * game_framework.frame_time
        if self.Gx1 <= -400:
            self.Gx1 = 1200
        self.Gx2 -= 100 * game_framework.frame_time
        if self.Gx2 <= -400:
            self.Gx2 = 1200
        self.Bx1 -= 200 * game_framework.frame_time
        if self.Bx1 <= -400:
            self.Bx1 = 1200
        self.Bx2 -= 200 * game_framework.frame_time
        if self.Bx2 <= -400:
            self.Bx2 = 1200
        self.Fx -= 100 * game_framework.frame_time
        if self.Fx <= - 800:
            self.Fx = 800