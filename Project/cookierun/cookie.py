from pico2d import *

import interface_state

# Cookie State
RUN, SLIDE, JUMP = range(3)

# Cookie Event
DOWN_DOWN, DOWN_UP, UP_DOWN, UP_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP
}

next_state_table = {
    RUN: {DOWN_DOWN: SLIDE, DOWN_UP: SLIDE, UP_DOWN: JUMP, UP_UP: JUMP},
    SLIDE: {DOWN_DOWN: RUN, DOWN_UP: RUN},
    JUMP: {UP_DOWN: JUMP, UP_UP: RUN}
}


class Cookie:
    def __init__(self):
        self.event_que = []
        self.x, self.y = 800 // 4, 102
        self.count = 0
        self.cur_state = RUN
        self.velocity = 0
        self.acceleration = 0.05
        self.speed = 0
        self.enter_state[RUN](self)
        if interface_state.CharChoice == 0:
            self.imageRun = load_image('BraveCookie_Move.png')
            self.imageSlide = load_image('BraveCookie_Slide.png')
            self.imageJump = load_image('BraveCookie_Jump.png')
        elif interface_state.CharChoice == 1:
            pass
        elif interface_state.CharChoice == 2:
            pass
        elif interface_state.CharChoice == 3:
            pass

    def gravity(self):
        self.y += self.speed
        self.speed -= self.acceleration

    # RUN state functions
    def enter_RUN(self):
        self.frame = 0

    def exit_RUN(self):
        pass

    def do_RUN(self):
        self.count = (self.count + 1) % 18
        if self.count == 0:
            self.frame = (self.frame + 1) % 4

    def draw_RUN(self):
        if self.velocity == 0:
            self.imageRun.clip_draw(self.frame * 64, 0, 64, 72, self.x, self.y)
            draw_rectangle(self.x - 32, self.y + 36, self.x + 32, self.y - 36)

    # SLIDE state functions
    def enter_SLIDE(self):
        self.frame = 0

    def jump_now(self):
        self.speed = 5

    def exit_SLIDE(self):
        pass

    def do_SLIDE(self):
        self.count = (self.count + 1) % 18
        if self.count == 0:
            self.frame = (self.frame + 1) % 2

    def draw_SLIDE(self):
        if self.velocity == -1:
            self.imageSlide.clip_draw(self.frame * 88, 0, 88, 36, self.x, self.y)
            draw_rectangle(self.x - 44, self.y + 18, self.x + 44, self.y - 18)

    # JUMP state functions
    def enter_JUMP(self):
        self.frame = 0

    def exit_JUMP(self):
        pass

    def do_JUMP(self):
        self.count = (self.count + 1) % 18
        if self.count == 0:
            self.frame = (self.frame + 1) % 2

    def draw_JUMP(self):
        if self.velocity == 1:
            self.imageJump.clip_draw(self.frame * 64, 0, 64, 60, self.x, self.y)
            draw_rectangle(self.x - 32, self.y + 30, self.x + 32, self.y - 30)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def change_state(self,  state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state

    enter_state = {RUN: enter_RUN, SLIDE: enter_SLIDE, JUMP: enter_JUMP}
    exit_state = {RUN: exit_RUN, SLIDE: exit_SLIDE, JUMP: exit_JUMP}
    do_state = {RUN: do_RUN, SLIDE: do_SLIDE, JUMP: do_JUMP}
    draw_state = {RUN: draw_RUN, SLIDE: draw_SLIDE, JUMP: draw_JUMP}

    def update(self):
        #if 0 <= self.velocity:
        #    self.gravity()
        #    if self.y < 170:
        #        self.y = 170
        #        self.velocity = 0
        self.do_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
        self.draw_state[self.cur_state](self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == DOWN_DOWN:
                self.velocity -= 1
                self.y -= 18
            elif key_event == DOWN_UP:
                self.velocity += 1
                self.y += 18
            if key_event == UP_DOWN:
                self.velocity += 1
                self.jump_now()
            elif key_event == UP_UP:
                self.velocity -= 1
            self.add_event(key_event)

