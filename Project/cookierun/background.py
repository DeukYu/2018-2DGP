from pico2d import *


class Background:
    def __init__(self):
        self.imageGround = load_image('First_ground.png')
        self.imageBackground = load_image('First_Background.png')

    def draw(self):
        self.imageBackground.draw(400, 250)
        self.imageGround.draw(400, 250)


    def update(self):
        pass