from pygame import *

BG color = (220, 100, 225)
WIDTH, HEIGHT = 600, 500

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Пинг понг')
mw.fill(BG_COLOR)

run = True
while run:


    for e in event.get():
        if e.type == QUIT
            run = False

    display.update()
    clock.tick(FPS)