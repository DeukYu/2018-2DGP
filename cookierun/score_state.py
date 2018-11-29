import game_framework
import interface_state
import game_world
from pico2d import *
import main_state


name = "PauseState"
imagePause = None
imageResume = None
imageEsc = None
Resume_Motion = None
Esc_Motion = None


def enter():
    global imagePause, imageResume, imageEsc, Resume_Motion, Esc_Motion
    imagePause = load_image('resource/pause/Pause.png')
    imageResume = load_image('resource/pause/Resume.png')
    imageEsc = load_image('resource/pause/Esc.png')
    Resume_Motion = 0
    Esc_Motion = 0


def exit():
    global imagePause, imageResume, imageEsc
    del imagePause
    del imageResume
    del imageEsc


def handle_events():
    global x, y, Resume_Motion, Esc_Motion
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()

            if(event.type, event.key) == (SDL_MOUSEMOTION, None):
                x, y = event.x, 500 - event.y - 1
                if 400 - 148 <= x <= 400 + 148:
                    if 313 - 47 <= y <= 313 + 47:
                        Resume_Motion = 1
                    else:
                        Resume_Motion = 0
                    if 186 - 47 <= y <= 186 + 47:
                        Esc_Motion = 1
                    else:
                        Esc_Motion = 0
                else:
                    Resume_Motion = 0
                    Esc_Motion = 0
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if Resume_Motion == 1:
                    print('resume')
                    game_framework.pop_state()
                elif Esc_Motion == 1:
                    print('esc')
                    game_world.clear()
                    game_framework.change_state(interface_state)
                else:
                    pass


def draw():
    clear_canvas()
    imagePause.draw(400, 250)
    if Resume_Motion == 1:
        imageResume.draw(400, 313)
    if Esc_Motion == 1:
        imageEsc.draw(400, 186)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






