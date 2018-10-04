from pico2d import *
import random
import turtle

KPU_WIDTH, KPU_HEIGHT = 800, 600

point = [(random.randint(0, 800), random.randint(0, 600)) for i in range(10)]


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
    character.clip_draw(frame * 100, 100 * 0, 100, 100, p[0], p[1])
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()


def draw_curve_11_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        move_point((x, y))

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i % 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (-3 * t ** 3 + 4 * t ** 2 + t)
             * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (-3 * t ** 3 + 4 * t ** 2 + t)
             * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        move_point((x, y))

    # draw p3-p4
    for i in range(0, 100, 2):
        t = i % 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        move_point((x, y))

    # draw p4-p5
    for i in range(50, 100, 2):
        t = i % 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        move_point((x, y))
    # draw p5-p6
    for i in range(50, 100, 2):
        t = i % 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        move_point((x, y))
    # draw p6-p7

    # draw p7-p8

    # draw p8-p9

    # draw p9-p10

    # draw p10-p11


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
charx, chary = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0

while running:
    draw_curve_11_points(point[0], point[1], point[2], point[3], point[4], point[5], point[6], point[7], point[8], point[9], point[0])

close_canvas()