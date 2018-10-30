from pico2d import *

import interface_state
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Cookie Event
DOWN_DOWN, DOWN_UP, SPACE_DOWN, SPACE_UP, GROUND_IN = range(5)

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
            cookie.jump_saveY = cookie.y
            cookie.jump_now()
        elif event == DOWN_UP:
            pass
        elif event == SPACE_UP:
            pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(cookie):
        cookie.imageRun.clip_draw(int(cookie.frame) * 64, 0, 64, 72, cookie.x, cookie.y)
        draw_rectangle(cookie.x - 32, cookie.y + 36, cookie.x + 32, cookie.y - 36)


class SlideState:

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
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

    @staticmethod
    def draw(cookie):
        cookie.imageSlide.clip_draw(int(cookie.frame) * 88, 0, 88, 36, cookie.x, cookie.y)
        draw_rectangle(cookie.x - 44, cookie.y + 18, cookie.x + 44, cookie.y - 18)


class JumpState:

    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            pass
        elif event == SPACE_DOWN:
            cookie.jump_now()
        elif event == DOWN_UP:
            pass
        elif event == DOWN_DOWN:
            pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        cookie.ground_in()

    @staticmethod
    def draw(cookie):
        cookie.imageJump.clip_draw(int(cookie.frame) * 64, 0, 64, 60, cookie.x, cookie.y)
        draw_rectangle(cookie.x - 32, cookie.y + 30, cookie.x + 32, cookie.y - 30)


class AirJumpState:
    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            pass
        elif event == SPACE_DOWN:
            cookie.jump_now()
        elif event == DOWN_UP:
            pass
        elif event == SPACE_UP:
            pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        cookie.ground_in()

    @staticmethod
    def draw(cookie):
        cookie.imageAirJump.clip_draw(int(cookie.frame) * 64, 0, 64, 76, cookie.x, cookie.y)
        draw_rectangle(cookie.x - 32, cookie.y + 38, cookie.x + 32, cookie.y - 38)


next_state_table = {
    RunState: {DOWN_UP: SlideState, DOWN_DOWN: SlideState, SPACE_DOWN: JumpState, SPACE_UP: JumpState, GROUND_IN: RunState},
    SlideState: {DOWN_UP: RunState, DOWN_DOWN: RunState, SPACE_DOWN: SlideState, SPACE_UP: SlideState, GROUND_IN: RunState},
    JumpState: {DOWN_UP: JumpState, DOWN_DOWN: JumpState, SPACE_DOWN: AirJumpState, SPACE_UP: JumpState, GROUND_IN: RunState},
    AirJumpState: {DOWN_UP: AirJumpState, DOWN_DOWN: AirJumpState, SPACE_DOWN: AirJumpState, SPACE_UP: AirJumpState, GROUND_IN: RunState}
}


class Cookie:
    def __init__(self):
        self.event_que = []
        self.x, self.y = 200, 102
        self.count = 0
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.motion = 0
        self.acceleration = 0.03
        self.speed = 0
        self.frame = 0
        self.jump_saveY = 102
        self.frame = 0
        if interface_state.CharChoice == 0:
            self.imageRun = load_image('resource/character/BraveCookie_Move.png')
            self.imageSlide = load_image('resource/character/BraveCookie_Slide.png')
            self.imageJump = load_image('resource/character/BraveCookie_Jump.png')
            self.imageAirJump = load_image('resource/character/BraveCookie_DoubleJump.png')
        elif interface_state.CharChoice == 1:
            pass
        elif interface_state.CharChoice == 2:
            pass
        elif interface_state.CharChoice == 3:
            pass

    def jump_now(self):
        print("jump_now")
        self.speed += 3

    def gravity(self):
        self.y += self.speed
        print(self.y)
        self.speed -= self.acceleration

    def ground_in(self):
        self.gravity()
        if self.y <= self.jump_saveY:
            self.y = self.jump_saveY
            self.speed = 0
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

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

