import game_framework
from pico2d import *
import title_devsisters_state


name = "title_kakao"
image = None
kakao_time = 0.0


def enter():
    global image
    image = load_image('resource/title/title_kakao.png')


def exit():
    global image
    del(image)


def update():
    global kakao_time

    if kakao_time > 1.0:
        kakao_time = 0
        game_framework.change_state(title_devsisters_state)
    delay(0.01)
    kakao_time += 0.01


def draw():
    clear_canvas()
    image.draw(400, 250)
    update_canvas()


def handle_events():
    events = get_events()