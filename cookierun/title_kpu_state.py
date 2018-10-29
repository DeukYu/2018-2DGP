import game_framework
from pico2d import *
import title_kakao_state


name = "title_kpu"
image = None
kpu_time = 0.0


def enter():
    global image
    image = load_image('resource/title/title_kpu.png')


def exit():
    global image
    del image


def update():
    global kpu_time

    if kpu_time > 1.0:
        kpu_time = 0
        game_framework.change_state(title_kakao_state)
    delay(0.01)
    kpu_time += 0.01


def draw():
    clear_canvas()
    image.draw(400, 250)
    update_canvas()


def handle_events():
    events = get_events()



