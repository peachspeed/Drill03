from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#grass.draw_now(400, 30)


def run_rectangle():
    print('RECTANGLE')

    clear_canvas_now()
    character.draw_now(400, 300)

def run_circle():
    print('CIRCLE')
    pass


while True:
    run_circle()
    run_rectangle()
    break


close_canvas()

