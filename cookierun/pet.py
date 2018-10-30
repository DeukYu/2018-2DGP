from pico2d import *

import interface_state
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Pet:
    def __init__(self):
        self.x, self.y = 150, 102
        self.frame = 0

        if interface_state.PetChoice == 0:
            self.image = load_image('resource/pet/starofangle_idle.png')
        elif interface_state.PetChoice == 1:
            pass
        elif interface_state.PetChoice == 2:
            pass
        elif interface_state.PetChoice == 3:
            pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        self.image.clip_draw(int(self.frame) * 48, 0, 48, 32, self.x, self.y)
        draw_rectangle(self.x - 24, self.y + 16, self.x + 24, self.y - 16)

