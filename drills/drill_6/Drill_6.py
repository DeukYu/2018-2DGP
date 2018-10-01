from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 800, 600


def handle_events():
    # fill here
    global running  # 달리는 것
    global mx, my  # 마우스 위치
    global ax, ay  # 도착 위치
    global sx, sy  # 케릭터와 클릭지점의 거리
    global cx, cy  # 케릭터 위치
    global click   # 클릭시 bool값

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
                running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            ax, ay = event.x, KPU_HEIGHT - 1 - event.y
            sx, sy = ax - cx, ay - cy
            if click != True:
                click = True
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            click = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def character_dir(arrive_pos, character_pos):
    global way
    if arrive_pos < character_pos:
        way = 0
    elif arrive_pos > character_pos:
        way = 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
sx, sy = 0, 0
click = False
move_char = False
way = 1
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * way, 100, 100, cx, cy)
    mouse.clip_draw(0, 0, 50, 52, mx+25, my-30)
    update_canvas()
    frame = (frame + 1) % 8
    if click:
        character_dir(ax, cx)
        move_char = True
    if move_char:
        cx += sx * 0.1
        cy += sy * 0.1
        if ax - 3 < cx < ax + 3 and ay - 3 < cy < ay + 3:
            move_char = False
    delay(0.05)
    handle_events()


close_canvas()




