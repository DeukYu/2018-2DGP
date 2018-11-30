from pico2d import *

import interface_state
import game_framework
import game_world
import main_state
import score_state
import random

import stage

#기본적인 액션 타이머
TIME_PER_ACTION1 = 0.3
ACTION_PER_TIME1 = 1.0 / TIME_PER_ACTION1
# 이중 점프시 액션 타이머
TIME_PER_ACTION2 = 0.5
ACTION_PER_TIME2 = 1.0 / TIME_PER_ACTION2
TIME_PER_ACTION5 = 0.5
ACTION_PER_TIME5 = 1.0 / TIME_PER_ACTION5

FRAMES_PER_ACTION2 = 2
FRAMES_PER_ACTION4 = 4
FRAMES_PER_ACTION5 = 5
FRAMES_PER_ACTION7 = 7
FRAMES_PER_ACTION8 = 8

# Cookie Event
DOWN_DOWN, DOWN_UP, SPACE_DOWN, SPACE_UP, GROUND_IN, HIT, TIME_OVER = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

#Cookie State


class RunState:

    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            pass
        elif event == SPACE_DOWN:
            cookie.change_jump_bb()
            cookie.jump_saveY = cookie.y
            cookie.jump_now()
        elif event == DOWN_UP:
            cookie.change_run_bb()
            cookie.y += 20
        elif event == SPACE_UP:
            pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION4 * ACTION_PER_TIME1 * game_framework.frame_time) % 4

    @staticmethod
    def draw(cookie):
        if interface_state.CharChoice == 0:
            cookie.imageRun.clip_draw(int(cookie.frame) * 144, 480, 144, 160, cookie.x, cookie.y)
        elif interface_state.CharChoice == 1:
            cookie.imageRun.clip_draw(int(cookie.frame) * 144, 320, 144, 160, cookie.x, cookie.y)
        elif interface_state.CharChoice == 2:
            cookie.imageRun.clip_draw(int(cookie.frame) * 144, 160, 144, 160, cookie.x, cookie.y)
        elif interface_state.CharChoice == 3:
            cookie.imageRun.clip_draw(int(cookie.frame) * 144, 0, 144, 160, cookie.x, cookie.y)
        cookie.draw_bb()


class SlideState:

    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            cookie.change_slide_bb()
            cookie.y -= 20
        elif event == SPACE_DOWN:
            pass
        elif event == DOWN_UP:
            pass
        elif event == SPACE_UP:
            pass


    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION2 * ACTION_PER_TIME1 * game_framework.frame_time) % 2

    @staticmethod
    def draw(cookie):
        if interface_state.CharChoice == 0:
            cookie.imageSlide.clip_draw(int(cookie.frame) * 192, 366, 192, 122, cookie.x, cookie.y)
        elif interface_state.CharChoice == 1:
            cookie.imageSlide.clip_draw(int(cookie.frame) * 192, 244, 192, 122, cookie.x, cookie.y)
        elif interface_state.CharChoice == 2:
            cookie.imageSlide.clip_draw(int(cookie.frame) * 192, 122, 192, 122, cookie.x, cookie.y)
        elif interface_state.CharChoice == 3:
            cookie.imageSlide.clip_draw(int(cookie.frame) * 192, 0, 192, 122, cookie.x, cookie.y)
        cookie.draw_bb()


class JumpState:

    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            pass
        elif event == SPACE_DOWN:
            cookie.jump_now()
        elif event == DOWN_UP:
            pass
        elif event == SPACE_UP:
            cookie.change_jump_bb()

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION2 * ACTION_PER_TIME1 * game_framework.frame_time) % 2
        cookie.ground_in()

    @staticmethod
    def draw(cookie):
        if interface_state.CharChoice == 0:
            cookie.imageJump.clip_draw(int(cookie.frame) * 160, 576, 160, 192, cookie.x, cookie.y)
        elif interface_state.CharChoice == 1:
            cookie.imageJump.clip_draw(int(cookie.frame) * 160, 384, 160, 192, cookie.x, cookie.y)
        elif interface_state.CharChoice == 2:
            cookie.imageJump.clip_draw(int(cookie.frame) * 160, 192, 160, 192, cookie.x, cookie.y)
        elif interface_state.CharChoice == 3:
            cookie.imageJump.clip_draw(int(cookie.frame) * 160, 0, 160, 192, cookie.x, cookie.y)
        cookie.draw_bb()


class AirJumpState:
    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            pass
        elif event == SPACE_DOWN:
            if cookie.AirJump_Check == False:
                cookie.AirJump_Check = True
                cookie.jump_now()
                cookie.change_airjump_bb()
        elif event == DOWN_UP:
            pass
        elif event == SPACE_UP:
            pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION7 * ACTION_PER_TIME2 * game_framework.frame_time / 3.8) % 7
        cookie.ground_in()

    @staticmethod
    def draw(cookie):
        if interface_state.CharChoice == 0:
            cookie.imageAirJump.clip_draw(int(cookie.frame) * 160, 630, 160, 210, cookie.x, cookie.y)
        elif interface_state.CharChoice == 1:
            cookie.imageAirJump.clip_draw(int(cookie.frame) * 160, 420, 160, 210, cookie.x, cookie.y)
        elif interface_state.CharChoice == 2:
            cookie.imageAirJump.clip_draw(int(cookie.frame) * 160, 210, 160, 210, cookie.x, cookie.y)
        elif interface_state.CharChoice == 3:
            cookie.imageAirJump.clip_draw(int(cookie.frame) * 160, 0, 160, 210, cookie.x, cookie.y)
        cookie.draw_bb()


class TimeOverState:
    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            pass
        elif event == SPACE_DOWN:
            pass
        elif event == DOWN_UP:
            pass
        elif event == SPACE_UP:
            pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        if cookie.frame < 4:
            cookie.frame = (cookie.frame + FRAMES_PER_ACTION5 * ACTION_PER_TIME5 * game_framework.frame_time) % 5

        if cookie.frame > 4:
            if main_state.stage.operation:
                main_state.stage.operation = False
            if cookie.y > 155:
                cookie.y -= 5
            if cookie.y <= 155:
                delay(0.5)
                game_framework.push_state(score_state)

    @staticmethod
    def draw(cookie):
        if interface_state.CharChoice == 0:
            cookie.imageTimeOver.clip_draw(int(cookie.frame) * 320, 432, 320, 144, cookie.x, cookie.y)
        elif interface_state.CharChoice == 1:
            cookie.imageTimeOver.clip_draw(int(cookie.frame) * 320, 288, 320, 144, cookie.x, cookie.y)
        elif interface_state.CharChoice == 2:
            cookie.imageTimeOver.clip_draw(int(cookie.frame) * 320, 144, 320, 144, cookie.x, cookie.y)
        elif interface_state.CharChoice == 3:
            cookie.imageTimeOver.clip_draw(int(cookie.frame) * 320, 0, 320, 144, cookie.x, cookie.y)


class HitState:
    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            pass
        elif event == SPACE_DOWN:
            pass
        elif event == DOWN_UP:
            pass
        elif event == SPACE_UP:
            pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION2 * ACTION_PER_TIME2 * game_framework.frame_time) % 2
        if cookie.y > 155:
            cookie.y -= 5
        elif cookie.y <= 155:
            cookie.y = 155

        if get_time() - cookie.HitTime > 2 and cookie.y <= 155:
            main_state.stage.operation = True
            cookie.add_event(GROUND_IN)

    @staticmethod
    def draw(cookie):
        cookie.imageHit.opacify(0.1 * random.randint(1, 9))
        if interface_state.CharChoice == 0:
            cookie.imageHit.clip_draw(int(cookie.frame) * 176, 612, 176, 204, cookie.x, cookie.y)
        elif interface_state.CharChoice == 1:
            cookie.imageHit.clip_draw(int(cookie.frame) * 176, 408, 176, 204, cookie.x, cookie.y)
        elif interface_state.CharChoice == 2:
            cookie.imageHit.clip_draw(int(cookie.frame) * 176, 204, 176, 204, cookie.x, cookie.y)
        elif interface_state.CharChoice == 3:
            cookie.imageHit.clip_draw(int(cookie.frame) * 176, 0, 176, 204, cookie.x, cookie.y)
        cookie.imageHit.opacify(1.0)
        cookie.draw_bb()

next_state_table = {
    RunState: {DOWN_UP: SlideState, DOWN_DOWN: SlideState, SPACE_DOWN: JumpState, SPACE_UP: JumpState,
               GROUND_IN: RunState, TIME_OVER: TimeOverState, HIT: HitState},
    SlideState: {DOWN_UP: RunState, DOWN_DOWN: RunState, SPACE_DOWN: SlideState, SPACE_UP: SlideState,
                 GROUND_IN: RunState, TIME_OVER: TimeOverState, HIT: HitState},
    JumpState: {DOWN_UP: JumpState, DOWN_DOWN: JumpState, SPACE_DOWN: AirJumpState, SPACE_UP: JumpState,
                GROUND_IN: RunState, TIME_OVER: TimeOverState, HIT: HitState},
    AirJumpState: {DOWN_UP: AirJumpState, DOWN_DOWN: AirJumpState, SPACE_DOWN: AirJumpState, SPACE_UP: AirJumpState,
                   GROUND_IN: RunState, TIME_OVER: TimeOverState, HIT: HitState},
    TimeOverState: {DOWN_UP: TimeOverState, DOWN_DOWN: TimeOverState, SPACE_DOWN: TimeOverState, SPACE_UP: TimeOverState,
                    GROUND_IN: TimeOverState, TIME_OVER: TimeOverState, HIT: HitState},
    HitState: {DOWN_UP: HitState, DOWN_DOWN: HitState, SPACE_DOWN: HitState, SPACE_UP: HitState,
                    GROUND_IN: RunState, TIME_OVER: TimeOverState, HIT: HitState}

}


class Cookie:
    def __init__(self):
        self.event_que = []
        self.x, self.y = 250, 155
        self.count = 0
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.motion = 0
        self.acceleration = 1600
        self.speed = 1
        self.frame = 0
        self.jump_saveY = 155
        self.AirJump_Check = False
        self.bb_Left = 72
        self.bb_Right = 72
        self.bb_Up = 70
        self.bb_Down = 80
        self.imageRun = load_image('resource/character/Cookie_Run.png')
        self.imageSlide = load_image('resource/character/Cookie_Slide.png')
        self.imageJump = load_image('resource/character/Cookie_Jump.png')
        self.imageAirJump = load_image('resource/character/Cookie_AirJump.png')
        self.imageHit = load_image('resource/character/Cookie_Hit.png')
        self.imageTimeOver = load_image('resource/character/Cookie_Timeover.png')
        self.space_time = 0
        self.speed_down = False
        self.pace = 1

        self.jelly_cnt = 0
        self.coin_cnt = 0

        self.HitTime = 0
        self.HitCheck = False

        if interface_state.CharChoice == 0:
            self.FullHp = 110
            self.CurHp = 110
            self.Ability = 0
            self.pace = 1
        elif interface_state.CharChoice == 1:
            self.FullHp = 150
            self.CurHp = 150
            self.Ability = 1
            self.pace = 1.3
        elif interface_state.CharChoice == 2:
            self.FullHp = 160
            self.CurHp = 160
            self.Ability = 2
            self.pace = 1
        elif interface_state.CharChoice == 3:
            self.FullHp = 150
            self.CurHp = 150
            self.Ability = 3
            self.pace = 1

    def get_bb(self):
        return self.x - self.bb_Left, self.y - self.bb_Down, self.x + self.bb_Right, self.y + self.bb_Up

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def change_run_bb(self):
        self.bb_Left = 72
        self.bb_Right = 72
        self.bb_Up = 70
        self.bb_Down = 80

    def change_slide_bb(self):
        self.bb_Left = 72
        self.bb_Right = 72
        self.bb_Up = 10
        self.bb_Down = 64

    def change_jump_bb(self):
        self.bb_Left = 65
        self.bb_Right = 65
        self.bb_Up = 10
        self.bb_Down = 90

    def change_airjump_bb(self):
        self.bb_Left = 60
        self.bb_Right = 60
        self.bb_Up = 40
        self.bb_Down = 80

    def jump_now(self):
        self.speed = 800

    def gravity(self):
        self.space_time = get_time() - main_state.game_timer
        self.speed_down = 1 - self.speed_down
        if self.speed_down:
            self.speed -= self.acceleration * self.space_time * 2
        self.y += self.speed * self.space_time

    def ground_in(self):
        self.gravity()
        if self.y <= self.jump_saveY:
            self.y = self.jump_saveY
            self.speed = 0
            self.AirJump_Check = False
            self.change_run_bb()
            self.add_event(GROUND_IN)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        main_state.game_timer = get_time()
        if get_time() - main_state.hp_time >= 0.2 and self.CurHp > 0:
            self.CurHp -= 1
            main_state.hp_time = get_time()
        elif get_time() - main_state.hp_time >= 0.2 and self.CurHp <= 0:
            self.add_event(TIME_OVER)

        if self.HitCheck:
            self.add_event(HIT)
            self.HitCheck = False

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

