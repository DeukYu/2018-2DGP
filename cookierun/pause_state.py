import game_framework
from pico2d import *
import main_state


name = "PauseState"
imagePause = None
imageResume = None
imageEsc = None


def enter():
    global imagePause, imageResume, imageEsc
    imagePause = load_image('resource/pause/Pause.png')
    imageResume = load_image('resource/pause/Resume.png')
    imageEsc = load_image('resource/pause/Esc.png')


def exit():
    global imagePause, imageResume, imageEsc
    del imagePause
    del imageResume
    del imageEsc


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()


def draw():
    clear_canvas()
    imagePause.draw(400, 250)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






