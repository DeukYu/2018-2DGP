import game_framework
import main_state
import game_world
import obstacles
import random
import items
import time
import cookie

from pico2d import *

class Stage:
    def __init__(self):
        self.image_Stage2_BackGround = load_image('resource/stage/Second_Background.png')
        self.image_Stage2_FrontGround = load_image('resource/stage/Second_Frontground.png')
        self.image_Stage2_BottomGround = load_image('resource/stage/Second_bottom.png')

        self.Bx1_1 = 400
        self.Bx1_2 = 1200
        self.Fx1_1 = 700
        self.Fx1_2 = 2100
        self.Bottomx1_1 = 400
        self.Bottomx1_2 = 1200
        self.timer = get_time()
        self.Creat_timer = get_time()
        self.ob_creat = False
        self.operation = True

        self.bgm = load_music('resource/sound/bgm_stage.ogg')
        self.bgm.set_volume(128)
        self.bgm.repeat_play()

        self.item_timer = get_time()


    def draw(self):
        self.image_Stage2_BackGround.draw(self.Bx1_1, 250, 800, 500)
        self.image_Stage2_BackGround.draw(self.Bx1_2, 250, 800, 500)

        self.image_Stage2_FrontGround.draw(self.Fx1_1, 250, 1400, 500)
        self.image_Stage2_FrontGround.draw(self.Fx1_2, 250, 1400, 500)

        self.image_Stage2_BottomGround.clip_draw(0, 0, 800, 500, self.Bottomx1_1, 250, 800, 500)
        self.image_Stage2_BottomGround.clip_draw(0, 0, 800, 500, self.Bottomx1_2, 250, 800, 500)

    def update(self):
        if self.operation:
            if self.Bx1_1 <= - 400:
                self.Bx1_1 = 1200
                self.Bx1_1 -= 10 * game_framework.frame_time * main_state.cookie.pace
            else:
                self.Bx1_1 -= 10 * game_framework.frame_time * main_state.cookie.pace

            if self.Bx1_2 <= - 400:
                self.Bx1_2 = 1200
                self.Bx1_2 -= 10 * game_framework.frame_time * main_state.cookie.pace
            else:
                self.Bx1_2 -= 10 * game_framework.frame_time * main_state.cookie.pace

            if self.Fx1_1 <= - 700:
                self.Fx1_1 = self.Fx1_2 + 1400
                self.Fx1_1 -= 350 * game_framework.frame_time * main_state.cookie.pace
            else:
                self.Fx1_1 -= 350 * game_framework.frame_time * main_state.cookie.pace

            if self.Fx1_2 <= - 700:
                self.Fx1_2 = self.Fx1_1 + 1400
                self.Fx1_2 -= 350 * game_framework.frame_time * main_state.cookie.pace
            else:
                self.Fx1_2 -= 350 * game_framework.frame_time * main_state.cookie.pace

            if self.Bottomx1_1 <= - 400:
                self.Bottomx1_1 = 1200
                self.Bottomx1_1 -= 250 * game_framework.frame_time * main_state.cookie.pace
            else:
                self.Bottomx1_1 -= 250 * game_framework.frame_time * main_state.cookie.pace

            if self.Bottomx1_2 <= - 400:
                self.Bottomx1_2 = 1200
                self.Bottomx1_2 -= 250 * game_framework.frame_time * main_state.cookie.pace
            else:
                self.Bottomx1_2 -= 250 * game_framework.frame_time * main_state.cookie.pace

            if (get_time() - self.item_timer) % 1 < 0.1:
                item = items.Items(random.randint(0, 2))
                game_world.add_object(item, 1)

            if (get_time() - self.item_timer) % 1 < 0.00001:
                item = items.Items(random.randint(3, 4))
                game_world.add_object(item, 1)

            if (get_time() - self.timer) % 1 < 0.01:
                if self.ob_creat == False:
                    obstacle = obstacles.Obstacles(random.randint(0, 4))
                    game_world.add_object(obstacle, 1)
                    self.ob_creat = True

            if (get_time() - self.Creat_timer) % 10 > 8.0:
                self.ob_creat = False
