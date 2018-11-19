import random
import json
import os

from pico2d import *
import game_framework
import game_world
import pause_state

from cookie import Cookie
from stage import Stage
from pet import Pet

name = "MainState"

cookie = None
background = None
pet = None
game_timer = None

def enter():
    global cookie, stage, pet, game_timer
    cookie = Cookie()
    stage = Stage()
    pet = Pet()
    game_timer = get_time()
    game_world.add_object(stage, 0)
    game_world.add_object(cookie, 1)
    game_world.add_object(pet, 2)


def exit():
    game_world.clear()


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
          game_framework.change_state(pause_state)
       else:
           cookie.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True





