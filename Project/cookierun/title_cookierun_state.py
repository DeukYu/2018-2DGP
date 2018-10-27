import game_framework
from pico2d import *
import interface_state


name = "title_cookierun"
image = None


def enter():
    global image
    image = load_image('resouce/title/title_cookieRun.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(interface_state)

def draw():
    clear_canvas()
    image.draw(400, 250)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






