import pygame
import math
import random
import time
import sys

# CONSTANTS
WIDTH = 640
HEIGHT = 640
PIXELS = 32
SQUARES_X = WIDTH // PIXELS
SQUARES_Y = HEIGHT // PIXELS

# COLORS
BG1 = (156, 210, 54)
BG2 = (147, 203, 57)
RED = (255, 0, 0)
BLUE = (0, 0, 50)
BLACK = (0, 0, 0)

class Snake:

    def __init__(self):
        self.color = BLUE
        self.headX = random.randrange(0, WIDTH, PIXELS)
        self.headY = random.randrange(0, HEIGHT, PIXELS)
        self.bodies = []
        self.body_color = 50
        self.state = "STOP"  # STOP, UP, DOWN, RIGHT, LEFT

    def move_head(self):
        if self.state == "UP":
            self.headY -= PIXELS
        elif self.state == "DOWN":
            self.headY += PIXELS
        elif self.state == "RIGHT":
            self.headX += PIXELS
        elif self.state == "LEFT":
            self.headX -= PIXELS

    def move_body(self):
        if len(self.bodies) > 0:
            for i in range(len(self.bodies)-1, -1, -1):
                if i == 0:
                    self.bodies[0].posX = self.headX
                    self.bodies[0].posY = self.headY
                else:
                    self.bodies[i].posX = self.bodies[i-1].posX
                    self.bodies[i].posY = self.bodies[i-1].posY

    def add_body(self):
        self.body_color += 10
        body = Body((0, 0, self.body_color), self.headX, self.headY)
        self.bodies.append(body)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.headX, self.headY, PIXELS, PIXELS))
        if len(self.bodies) > 0:
            for body in self.bodies:
                body.draw(surface)

    def die(self):
        self.headX = random.randrange(0, WIDTH, PIXELS)
        self.headY = random.randrange(0, HEIGHT, PIXELS)
        self.bodies = []
        self.body_color = 50
        self.state = "STOP"

class Body:

    def __init__(self, color, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS))

class Apple:

    def __init__(self):
        self.color = RED
        self.spawn()

    def spawn(self):
        while True:
            self.posX = random.randrange(0, WIDTH, PIXELS)
            self.posY = random.randrange(0, HEIGHT, PIXELS)
            if not any(body.posX == self.posX and body.posY == self.posY for body in snake.bodies) and (self.posX, self.posY) != (snake.headX, snake.headY):
                break

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS))

class Background:

    def draw(self, surface):
        surface.fill(BG1)
        counter = 0
        for row in range(SQUARES_Y):
            for col in range(SQUARES_X):
                if counter % 2 == 0:
                    pygame.draw.rect(surface, BG2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS))
                if col != SQUARES_X - 1:
                    counter += 1

class Collision:

    def between_snake_and_apple(self, snake, apple):
        return snake.headX == apple.posX and snake.headY == apple.posY

    def between_snake_and_walls(self, snake):
        return snake.headX < 0 or snake.headX >= WIDTH or snake.headY < 0 or snake.headY >= HEIGHT

    def between_head_and_body(self, snake):
        return any(snake.headX == body.posX and snake.headY == body.posY for body in snake.bodies)

class Score:

    def __init__(self):
        self.points = 0
        self.level = 1
        self.food_counter = 0
        self.font = pygame.font.SysFont('monospace', 30, bold=False)

    def increase(self):
        self.points += 1
        self.food_counter += 1
        if self.food_counter % 3 == 0:
            self.level += 1

    def reset(self):
        self.points = 0
        self.level = 1
        self.food_counter = 0

    def show(self, surface):
        lbl = self.font.render(f'Score: {self.points} Level: {self.level}', 1, BLACK)
        surface.blit(lbl, (5, 5))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SNAKE")
    global snake
    
    # OBJECTS
    snake = Snake()
    apple = Apple()
    background = Background()
    collision = Collision()
    score = Score()
    speed = 130
    
    while True:
        background.draw(screen)
        snake.draw(screen)
        apple.draw(screen)
        score.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.state != "DOWN":
                    snake.state = "UP"
                elif event.key == pygame.K_DOWN and snake.state != "UP":
                    snake.state = "DOWN"
                elif event.key == pygame.K_RIGHT and snake.state != "LEFT":
                    snake.state = "RIGHT"
                elif event.key == pygame.K_LEFT and snake.state != "RIGHT":
                    snake.state = "LEFT"
                elif event.key == pygame.K_p:
                    snake.state = "STOP"

        if collision.between_snake_and_apple(snake, apple):
            apple.spawn()
            snake.add_body()
            score.increase()
            speed = max(70, 130 - (score.level * 10))

        if snake.state != "STOP":
            snake.move_body()
            snake.move_head()

        if collision.between_snake_and_walls(snake) or collision.between_head_and_body(snake):
            snake.die()
            apple.spawn()
            score.reset()
            speed = 130

        pygame.time.delay(speed)
        pygame.display.update()

main()
