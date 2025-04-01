import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

# Create a background surface to store drawings
background = pygame.Surface(screen.get_size())
background.fill(WHITE)

# Load button icons
icon_size = (40, 40)
pen_icon = pygame.image.load("office-material.png")
pen_icon = pygame.transform.scale(pen_icon, icon_size)
rect_icon = pygame.image.load("frame.png")
rect_icon = pygame.transform.scale(rect_icon, icon_size)
circle_icon = pygame.image.load("circle.png")
circle_icon = pygame.transform.scale(circle_icon, icon_size)
eraser_icon = pygame.image.load("eraser.png")
eraser_icon = pygame.transform.scale(eraser_icon, icon_size)
color_icon = pygame.image.load("paint-palette.png")
color_icon = pygame.transform.scale(color_icon, icon_size)
clear_icon = pygame.image.load("clear.png")  # Load clear button icon
clear_icon = pygame.transform.scale(clear_icon, icon_size)

# Button positions
buttons = {
    "pen": (10, 10, pen_icon),
    "rect": (60, 10, rect_icon),
    "circle": (110, 10, circle_icon),
    "eraser": (160, 10, eraser_icon),
    "color": (210, 10, color_icon),
    "clear": (260, 10, clear_icon)  # Add clear button
}

# Variables
drawing = False
last_pos = None
color = BLACK
brush_size = 5
tool = "pen"  # Options: "pen", "rect", "circle", "eraser", "color", "clear"
start_pos = None

# Main loop
running = True
while running:
    screen.blit(background, (0, 0))  # Keep previous drawings
    
    for key, (x, y, icon) in buttons.items():
        screen.blit(icon, (x, y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for key, (x, y, icon) in buttons.items():
                    if x <= event.pos[0] <= x + icon_size[0] and y <= event.pos[1] <= y + icon_size[1]:
                        if key == "color":
                            color = [random.randint(0, 255) for _ in range(3)]  # Random color selection
                            pygame.draw.rect(background, color, (WIDTH - 50, 10, 40, 40))  # Display selected color
                        elif key == "clear":
                            background.fill(WHITE)  # Clear the screen
                        else:
                            tool = key
                        break
                else:
                    drawing = True
                    last_pos = event.pos
                    start_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if tool == "rect":
                    rect_x, rect_y = start_pos
                    end_x, end_y = event.pos
                    pygame.draw.rect(background, color, (rect_x, rect_y, end_x - rect_x, end_y - rect_y), 2)
                elif tool == "circle":
                    cx, cy = start_pos
                    radius = max(abs(event.pos[0] - cx), abs(event.pos[1] - cy))
                    pygame.draw.circle(background, color, start_pos, radius, 2)

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "pen":
                    pygame.draw.line(background, color, last_pos, event.pos, brush_size)
                    last_pos = event.pos
                elif tool == "eraser":
                    pygame.draw.line(background, WHITE, last_pos, event.pos, brush_size)
                    last_pos = event.pos
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_p:
                tool = "pen"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_x:  # Key to clear the screen
                background.fill(WHITE)
            elif event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)
    
    pygame.draw.rect(background, color, (WIDTH - 50, 10, 40, 40))  # Display selected color
    pygame.display.flip()

pygame.quit()
