import pygame as pg
from random import randint
pg.init()
disp = pg.display.set_mode((800,480))
pg.display.set_caption("Змейка!")
pg.display.update()

x = 200
y = 320
apple_x = 400
apple_y = 120
score = 0
snake = [[x,y]]
font = pg.font.Font(None, 40)

direction = "right"

game_over = False
clock = pg.time.Clock()

while not game_over:
    clock.tick(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                direction = "up"
            if event.key == pg.K_DOWN:
                direction = "down"
            if event.key == pg.K_LEFT:
                direction = "left"
            if event.key == pg.K_RIGHT:
                direction = "right"
    if direction == "left":
        x -= 40
    if direction == "right":
        x += 40
    if direction == "up":
        y -= 40
    if direction == "down":
        y += 40
    for  i in range(0, len(snake)-1):
        snake[i]=snake[i-1]
    snake[-1] = [x,y]
    if x == apple_x and y == apple_y:
        snake = [snake[0]]+snake
        score += 1
    while [apple_x, apple_y] in snake:
        apple_x = randint(1,19)*40
        apple_y = randint(1, 11) * 40
    disp.fill((0,0,0))

    for i in range(0, len(snake)):
        pg.draw.rect(disp, (0,255,0),[snake[i][0], snake[i][1], 40, 40])
    '''pg.draw.rect(disp,(0,255,0),[x,y,40,40])'''
    pg.draw.rect(disp, (255,0,0),[apple_x,apple_y,40,40])
    message = font.render('Счёт:' + str(score), True, (0,120,255))
    disp.blit(message, [0,0])

    pg.display.update()
pg.quit()
quit()
