import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.Clock()

game_over = False
score = 0  # Variável de pontuação inicial

font = pygame.font.Font(None, 36)
score_text = font.render(f'Score: {score}', True, (255, 255, 255))
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1  # Incrementa a pontuação quando a cobra come uma maçã

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    if (
        snake[0][0] < 0
        or snake[0][0] >= 600
        or snake[0][1] < 0
        or snake[0][1] >= 600
    ):
        game_over = True

    for segment in snake[1:]:
        if collision(snake[0], segment):
            game_over = True

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    # Atualiza o texto de pontuação a cada quadro
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, score_rect)  # Blit o texto de pontuação na tela

    pygame.display.update()

font = pygame.font.Font(None, 36)
game_over_text = font.render('Game Over', True, (255, 255, 255))
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (300, 300)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()

pygame.time.wait(2000)
pygame.quit()
