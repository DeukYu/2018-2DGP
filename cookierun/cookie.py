from pico2d import *

import interface_state

# Cookie Event
DOWN_DOWN, DOWN_UP, SPACE, GROUND_IN = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

#Cookie State

class RunState:

    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            cookie.motion = -1
        elif event == SPACE:
            cookie.motion = 1
        elif event == DOWN_UP:
            cookie.motion = 0
        cookie.timer = 0

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.timer = (cookie.timer + 1) % 18
        if cookie.timer == 0:
            cookie.frame = (cookie.frame + 1) % 4

    @staticmethod
    def draw(cookie):
        if cookie.motion == 0:
            cookie.imageRun.clip_draw(cookie.frame * 64, 0, 64, 72, cookie.x, cookie.y)
            draw_rectangle(cookie.x - 32, cookie.y + 36, cookie.x + 32, cookie.y - 36)


class SlideState:

    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            cookie.motion = -1
        elif event == SPACE:
            cookie.motion = 0
        elif event == DOWN_UP:
            cookie.motion = 0


    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.timer = (cookie.timer + 1) % 18
        if cookie.timer == 0:
            cookie.frame = (cookie.frame + 1) % 2

    @staticmethod
    def draw(cookie):
        if cookie.motion == -1:
            cookie.imageSlide.clip_draw(cookie.frame * 88, 0, 88, 36, cookie.x, cookie.y)
            draw_rectangle(cookie.x - 44, cookie.y + 18, cookie.x + 44, cookie.y - 18)


class JumpState:

    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            cookie.motion = 1
        elif event == SPACE:
            cookie.motion = 2
        elif event == DOWN_UP:
            cookie.motion = 0

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.timer = (cookie.timer + 1) % 18
        if cookie.timer == 0:
            cookie.frame = (cookie.frame + 1) % 2

    @staticmethod
    def draw(cookie):
        if cookie.motion == 1:
            cookie.imageJump.clip_draw(cookie.frame * 64, 0, 64, 60, cookie.x, cookie.y)
            draw_rectangle(cookie.x - 32, cookie.y + 30, cookie.x + 32, cookie.y - 30)


class AirJumpState:
    @staticmethod
    def enter(cookie, event):
        if event == DOWN_DOWN:
            cookie.motion = 2
        elif event == SPACE:
            cookie.motion = 2
        elif event == DOWN_UP:
            cookie.motion = 2

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.timer = (cookie.timer + 1) % 18
        if cookie.timer == 0:
            cookie.frame = (cookie.frame + 1) % 2

    @staticmethod
    def draw(cookie):
        if cookie.motion == 2:
            cookie.imageAirJump.clip_draw(cookie.frame * 64, 0, 64, 76, cookie.x, cookie.y)
            draw_rectangle(cookie.x - 32, cookie.y + 38, cookie.x + 32, cookie.y - 38)


next_state_table = {
    RunState: {DOWN_UP: SlideState, DOWN_DOWN: SlideState, SPACE: JumpState, GROUND_IN: RunState},
    SlideState: {DOWN_UP: RunState, DOWN_DOWN: RunState, SPACE: SlideState, GROUND_IN: SlideState},
    JumpState: {DOWN_UP: JumpState, DOWN_DOWN: JumpState, SPACE: AirJumpState, GROUND_IN: RunState},
    AirJumpState: {DOWN_UP: AirJumpState, DOWN_DOWN: AirJumpState, SPACE: AirJumpState, GROUND_IN: RunState}
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
        if interface_state.CharChoice == 0:
            self.imageRun = load_image('resource/character/BraveCookie_Move.png')
            self.imageSlide = load_image('resource/character/BraveCookie_Slide.png')
            self.imageJump = load_image('resource/character/BraveCookie_Jump.png')
            self.imageDoubleJump = load_image('resource/character/BraveCookie_DoubleJump.png')
        elif interface_state.CharChoice == 1:
            pass
        elif interface_state.CharChoice == 2:
            pass
        elif interface_state.CharChoice == 3:
            pass

    def jump_now(self):
        self.speed = 3

    def gravity(self):
        self.y += self.speed
        self.speed -= self.acceleration

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

