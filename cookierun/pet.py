from pico2d import *

import interface_state
import game_framework
import main_state
import cookie

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
STAR_FRAMES_PER_ACTION = 4
FLOWER_FRAMES_PER_ACTION = 7

class Pet:
    def __init__(self):
        self.x, self.y = 150, 102
        self.frame = 0

        if interface_state.PetChoice == 0:
            self.image = load_image('resource/pet/starofangle_idle.png')
        elif interface_state.PetChoice == 1:
            self.image = load_image('resource/pet/flower_idle.png')
            pass
        elif interface_state.PetChoice == 2:
            pass
        elif interface_state.PetChoice == 3:
            pass

    def update(self):
        if interface_state.PetChoice == 0:
            self.frame = (self.frame + STAR_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        elif interface_state.PetChoice == 1:
            self.frame = (self.frame + FLOWER_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        self.y = main_state.cookie.y

    def draw(self):
        if interface_state.PetChoice == 0:
            self.image.clip_draw(int(self.frame) * 48, 0, 48, 32, self.x, self.y)
            draw_rectangle(self.x - 24, self.y + 16, self.x + 24, self.y - 16)
        elif interface_state.PetChoice == 1:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y)
            draw_rectangle(self.x - 16, self.y + 16, self.x + 16, self.y - 16)
