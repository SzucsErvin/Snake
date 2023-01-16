import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10),Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos,cell_size, cell_size)
            pygame.draw.rect(screen, (244,122,122), block_rect)

class APPLE:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

    def draw_apple(self):
        apple_rect = pygame.Rect(int(self.pos.x * cell_size) ,int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,155,110),apple_rect)

pygame.init()
cell_size =  40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

apple = APPLE()
snake = SNAKE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,215,70))
    apple.draw_apple()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60),

    