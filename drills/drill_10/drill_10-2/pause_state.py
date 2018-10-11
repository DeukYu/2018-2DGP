import game_framework
from pico2d import *
import main_state
import title_state


name = "PauseState"
image = None

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.switch = 0

    def draw(self):
        if self.switch == 1:
            self.image.draw(400, 300)

    def update(self):
        self.switch = (self.switch + 1) % 2
        delay(0.05)


def enter():
    global image
    image = Pause()


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_state(title_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    image.draw()
    update_canvas()


def update():
    image.update()


def pause():
    pass


def resume():
    pass






