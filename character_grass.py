from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

x = 500
while (1):
    while (x <= 790):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y = 90
    while (y < 500):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(790, y)
        y = y + 2
        delay(0.01)

    while (x > 500):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 1
        x = x - 1
        delay(0.01)


    cx, cy = 400, 300 
    r = 200 
    angle = 0 

    while(1):
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)

        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        angle += 0.05  
        if angle >= 2 * math.pi:
            angle = 0

        delay(0.01)

close_canvas()
