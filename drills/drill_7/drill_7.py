from pico2d import *
import random
import turtle

KPU_WIDTH, KPU_HEIGHT = 800, 600

point = [(random.randint(0, 800), random.randint(0, 600)) for i in range(20)]


def handle_events():
    # fill here
    global running  # 달리는 것

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
                running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move_point(p):
    global frame
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * way, 100, 100, p[0], p[1])
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()


def draw_line(p1,p2):
    global way
    if p2[0] > p1[0]:
        way = 1
    elif p2[0] < p1[0]:
        way = 0
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1-t)*p1[0] + t * p2[0]
        y = (1-t)*p1[1] + t * p2[1]
        move_point((x,y))


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
charx, chary = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
way = 1
size = len(point)
n = 1

while running:
    draw_line(point[n-1],point[n])
    n = (n + 1) % size
close_canvas()
