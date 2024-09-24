from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def run_rectangle():
  
    run_top()
    run_right()
    run_bottom()
    run_left()


def run_top():
    x, y = 400, 90
    for i in range(90, 600, 10): 
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, i)
        delay(0.01)


def run_right():
    x, y = 400, 600
    for i in range(400, 800, 10): 
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(i, y)
        delay(0.01)


def run_bottom():
    x, y = 800, 600
    for i in range(600, 90, -10): 
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, i)
        delay(0.01)


def run_left():
    x, y = 800, 90
    for i in range(800, 400, -10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(i, y)
        delay(0.01)


def run_circle():
    r, cx, cy = 200, 400, 300 
    for d in range(0, 360, 5): 
        x = cx + r * math.cos(math.radians(d))
        y = cy + r * math.sin(math.radians(d))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)


def run_triangle():

    x1, y1 = 400, 500 
    x2, y2 = 200, 100  
    x3, y3 = 600, 100 


    for i in range(0, 100, 2):
        x = x1 + (x2 - x1) * i / 100
        y = y1 + (y2 - y1) * i / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)


    for i in range(0, 100, 2):
        x = x2 + (x3 - x2) * i / 100
        y = y2 + (y3 - y2) * i / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)


    for i in range(0, 100, 2):
        x = x3 + (x1 - x3) * i / 100
        y = y3 + (y1 - y3) * i / 100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)


while True:
    run_rectangle()  
    run_circle()     
    run_triangle()   

close_canvas()
