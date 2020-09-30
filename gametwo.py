import pygame as pg
pg.init()
win=pg.display.set_mode((500,500))
pg.display.set_caption("bigo")
x=50
y=430
width=40
height=60
vel=5
isjump=False
jumpcou=10
run=True
while run:
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False

    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT] and x>vel:
        x-=vel
    if keys[pg.K_RIGHT] and x<500-width-vel:
        x+=vel
    if not(isjump):
        if keys[pg.K_UP] and y>vel:
            y-=vel
        if keys[pg.K_DOWN] and y<500-height-vel:
            y+=vel
        if keys[pg.K_SPACE]:
            isjump = True
    else:
        if jumpcou >= -10:
            neg=1
            if jumpcou<0:
                neg=-1
            y -= (jumpcou**2)*0.5*neg
            jumpcou -= 1
        else:
            isjump=False
            jumpcou=10
            
    win.fill((0,0,0))    
    pg.draw.rect(win,(255,0,0),(int(x),int(y),int(width),int(height)))
    pg.display.update()


pg.quit()
