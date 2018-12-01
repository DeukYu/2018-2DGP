import game_framework
import interface_state
import game_world
from pico2d import *
import main_state


name = "score_State"
imageScore = None
ImageButton = None
Button_Motion = None
ScoreFont = None
Coin_Jelly_Font = None
Sound = None


def enter():
    global imageScore, imageButton, Button_Motion, ScoreFont, Coin_Jelly_Font
    imageScore = load_image('resource/score/Result.png')
    imageButton = load_image('resource/score/Check_Button.png')
    ScoreFont = load_font('KL019.ttf', 72)
    Coin_Jelly_Font = load_font('KL019.ttf', 48)
    Button_Motion = 0


def exit():
    global imageScore, imageButton, Button_Motion, ScoreFont, Coin_Jelly_Font
    del imageScore
    del imageButton
    del Button_Motion
    del ScoreFont
    del Coin_Jelly_Font


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
    ScoreFont.draw(350, 290, '%d' % (main_state.cookie.jelly_cnt + main_state.cookie.coin_cnt), (0, 0, 255))
    Coin_Jelly_Font.draw(570, 180, '%d' % main_state.cookie.jelly_cnt, (0, 0, 0))
    Coin_Jelly_Font.draw(570, 225, '%d' % main_state.cookie.coin_cnt, (0, 0, 0))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






