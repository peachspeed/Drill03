from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#grass.draw_now(400, 30)


def run_rectangle():
    print('RECTANGLE')

    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800//2, 600//2

    for d in range(0, 360):
        x = r*math.cos(math.radians(d)) + cx
        y = r*math.sin(math.radians(d)) + cy
        
    clear_canvas_now()
    character.draw_now(x, y)


while True:
    run_circle()
    run_rectangle()


close_canvas()

