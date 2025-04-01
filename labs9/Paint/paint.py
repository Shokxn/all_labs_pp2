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
icons = {
    "pen": "office-material.png",
    "rect": "frame.png",
    "circle": "circle.png",
    "eraser": "eraser.png",
    "color": "paint-palette.png",
    "clear": "clear.png",
    "square": "stop.png",
    "right_triangle": "bleach.png",
    "equilateral_triangle": "equilateral.png",
    "rhombus": "rhombus.png",
}

# Scale icons
buttons = {}
x_pos = 10
for key, path in icons.items():
    icon = pygame.image.load(path)
    icon = pygame.transform.scale(icon, icon_size)
    buttons[key] = (x_pos, 10, icon)
    x_pos += 50  # Space between buttons

# Variables
drawing = False
last_pos = None
color = BLACK
brush_size = 5
tool = "pen"  # Current tool
start_pos = None

# Main loop
running = True
while running:
    screen.blit(background, (0, 0))  # Keep previous drawings
    
    # Draw buttons
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
                            color = [random.randint(0, 255) for _ in range(3)]
                        elif key == "clear":
                            background.fill(WHITE)
                        else:
                            tool = key
                        break
                else:
                    drawing = True
                    last_pos = event.pos
                    start_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos is not None:
                drawing = False
                end_pos = event.pos
                if tool == "rect":
                    pygame.draw.rect(background, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
                elif tool == "square":
                    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(background, color, (*start_pos, size, size), 2)
                elif tool == "circle":
                    radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.circle(background, color, start_pos, radius, 2)
                elif tool == "right_triangle":
                    pygame.draw.polygon(background, color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
                elif tool == "equilateral_triangle":
                    base_x1, base_y = start_pos
                    base_x2, _ = end_pos
                    side_length = abs(base_x2 - base_x1)
                    height = int((side_length * (3 ** 0.5)) / 2)
                    top_vertex = ((base_x1 + base_x2) // 2, base_y - height)
                    pygame.draw.polygon(background, color, [(base_x1, base_y), (base_x2, base_y), top_vertex], 2)
                elif tool == "rhombus":
                    dx = abs(end_pos[0] - start_pos[0])
                    dy = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(background, color, [(start_pos[0], start_pos[1] - dy), (start_pos[0] + dx, start_pos[1]), (start_pos[0], start_pos[1] + dy), (start_pos[0] - dx, start_pos[1])], 2)
        
        elif event.type == pygame.MOUSEMOTION:
            if drawing and last_pos is not None:
                if tool == "pen":
                    pygame.draw.line(background, color, last_pos, event.pos, brush_size)
                    last_pos = event.pos
                elif tool == "eraser":
                    pygame.draw.line(background, WHITE, last_pos, event.pos, brush_size)
                    last_pos = event.pos
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_e:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_d:
                tool = "rhombus"
            elif event.key == pygame.K_p:
                tool = "pen"
            elif event.key == pygame.K_x:
                background.fill(WHITE)
            elif event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)
    
    pygame.draw.rect(background, color, (WIDTH - 50, 10, 40, 40))  # Display selected color
    pygame.display.flip()

pygame.quit()
