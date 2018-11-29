import game_framework
import interface_state
import game_world
from pico2d import *
import main_state


name = "score_State"
imageScore = None
ImageButton = None
Button_Motion = None


def enter():
    global imageScore, imageButton, Button_Motion
    imageScore = load_image('resource/score/Result.png')
    imageButton = load_image('resource/score/Check_Button.png')
    Button_Motion = 0


def exit():
    global imageScore, imageButton, Button_Motion
    del imageScore
    del imageButton
    del Button_Motion


def handle_events():
    global x, y, Button_Motion
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()

            if(event.type, event.key) == (SDL_MOUSEMOTION, None):
                x, y = event.x, 500 - event.y - 1

                if 405 - 81 <= x <= 405 + 81:
                    if 115 - 26 <= y <= 115 + 26:
                        Button_Motion = 1
                    else:
                        Button_Motion = 0
                else:
                    Button_Motion = 0

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if Button_Motion == 1:
                    game_world.clear()
                    game_framework.change_state(interface_state)
                else:
                    pass


def draw():
    clear_canvas()
    imageScore.draw(400, 250)
    if Button_Motion == 1:
        imageButton.draw(405, 115)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






