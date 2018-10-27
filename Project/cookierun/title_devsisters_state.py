import game_framework
from pico2d import *
import title_cookierun_state


name = "title_devsisters"
image = None
devsisters_time = 0.0


def enter():
    global image
    image = load_image('resource/title/title_devsisters.png')


def exit():
    global image
    del(image)


def update():
    global devsisters_time

    if devsisters_time > 1.0:
        devsisters_time = 0
        game_framework.change_state(title_cookierun_state)
    delay(0.01)
    devsisters_time += 0.01


def draw():
    clear_canvas()
    image.draw(400, 250)
    update_canvas()


def handle_events():
    events = get_events()



