import pygame as pg
from random import randint
pg.init()
disp = pg.display.set_mode((800, 480))
pg.display.set_caption("Змейка!")
pg.display.update()

x = 200
y = 320
apple_x = 400
apple_y = 120
score = 0
snake = [[x, y]]
snake_body = pg.image.load("body.png")
snake_head_right = pg.image.load("head_right.png")
snake_head_left = pg.image.load("head_left.png")
snake_head_up = pg.image.load("head _up.png")
snake_head_down = pg.image.load("head_down.png")
apple = pg.image.load("apple.png")
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
    for i in range(0, len(snake)-1):
        snake[i] = snake[i+1]
    snake[-1] = [x, y]
    if x == apple_x and y == apple_y:
        snake = [snake[0]]+snake
        score += 1
        while [apple_x, apple_y] in snake:
            apple_x = randint(1, 19)*40
            apple_y = randint(1, 11) * 40
    disp.fill((0, 0, 0))
    for i in range(0, len(snake)):
        disp.blit(snake_body, [snake[i][0], snake[i][1]])
    if direction == "right":
        disp.blit(snake_head_right, [x, y])
    if direction == "left":
        disp.blit(snake_head_left, [x, y])
    if direction == "up":
        disp.blit(snake_head_up, [x, y])
    if direction == "down":
        disp.blit(snake_head_down, [x, y])

    disp.blit(apple, [apple_x, apple_y])

    message = font.render('Счёт:' + str(score), True, (0, 120, 255))
    disp.blit(message, [0, 0])

    pg.display.update()
pg.quit()
quit()
