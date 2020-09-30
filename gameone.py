import pygame as pg
pg.init()
win=pg.display.set_mode((500,500))
pg.display.set_caption("bigo")
x=50
y=50
width=40
height=60
vel=5

run=True
while run:
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False

    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x-=vel
    if keys[pg.K_RIGHT]:
        x+=vel
    if keys[pg.K_UP]:
        y-=vel
    if keys[pg.K_DOWN]:
        y+=vel
    win.fill((0,0,0))    
    pg.draw.rect(win,(255,0,0),(x,y,width,height))
    pg.display.update()


pg.quit()
