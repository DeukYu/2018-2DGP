from pico2d import *

import interface_state
import game_framework
import game_world
import main_state
import random
import items
import cookie

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
STAR_FLOWER_FRAMES_PER_ACTION = 4
GHOST_FRAMES_PER_ACTION = 3


class Pet:
    def __init__(self):
        self.x, self.y = 140, 102
        self.frame = 0
        self.Pet_Time = get_time()
        self.speed = 0
        self.Invincibility = False

        if interface_state.PetChoice == 0:
            self.image = load_image('resource/pet/starofangle_idle.png')
        elif interface_state.PetChoice == 1:
            self.image = load_image('resource/pet/flower_idle.png')
            self.speed = 0.5
        elif interface_state.PetChoice == 2:
            self.image = load_image('resource/pet/facebook_idle.png')
        elif interface_state.PetChoice == 3:
            self.image = load_image('resource/pet/ghost_idle.png')
            self.Invincibility = True

    def enter(self):
        pass

    def update(self):
        if interface_state.PetChoice == 0:
            self.frame = (self.frame + STAR_FLOWER_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if get_time() - self.Pet_Time > 5:
                for i in range(0, 10):
                    item = items.Items(random.randint(0, 2), random.randint(100, 700))
                    game_world.add_object(item, 1)
                    self.Pet_Time = get_time()

        elif interface_state.PetChoice == 1:
            self.frame = (self.frame + STAR_FLOWER_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        elif interface_state.PetChoice == 2:
            self.frame = (self.frame + STAR_FLOWER_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if get_time() - self.Pet_Time > 15:
                item = items.Items(random.randint(3, 4), 400)
                game_world.add_object(item, 1)
                self.Pet_Time = get_time()

        elif interface_state.PetChoice == 3:
            self.frame = (self.frame + GHOST_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        self.y = main_state.cookie.y + 15

    def draw(self):
        if interface_state.PetChoice == 0:
            self.image.clip_draw(int(self.frame) * 48, 0, 48, 32, self.x, self.y)
            #draw_rectangle(self.x - 24, self.y + 16, self.x + 24, self.y - 16)

        elif interface_state.PetChoice == 1:
            self.image.clip_draw(int(self.frame) * 48, 0, 48, 64, self.x, self.y)
            #draw_rectangle(self.x - 24, self.y + 32, self.x + 24, self.y - 32)

        elif interface_state.PetChoice == 3:
            self.image.clip_draw(int(self.frame) * 48, 0, 48, 48, self.x, self.y)
            #draw_rectangle(self.x - 24, self.y + 24, self.x + 24, self.y - 24)
