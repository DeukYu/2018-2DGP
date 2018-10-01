import os
from pico2d import *
from math import *

Angle = 270 * (pi/180);

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
Dir = 0
x = 400
y = 90
r = 210
count = 0;

while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if(Dir == 0):
        x += 2
        delay(0.01)
        if(x >= 780):
            Dir = 1
    elif(Dir == 1):
        y += 2
        delay(0.01)
        if(y >= 550):
            Dir = 2
    elif(Dir == 2):
        x -= 2
        delay(0.01)
        if(x <= 20):
            Dir = 3
    elif(Dir == 3):
        y -= 2
        delay(0.01)
        if(y <= 90):
            Dir = 4
    elif(Dir == 4):
        x += 2
        delay(0.01)
        if(x >= 400):
            Dir = 5
    elif(Dir == 5):
        x = 400
        y = 300
        x += r * cos(Angle)
        y += r * sin(Angle)
        count += 1
        Angle += pi / 180
        delay(0.01)
        if(count == 360):
            Dir = 0
        
close_canvas()

