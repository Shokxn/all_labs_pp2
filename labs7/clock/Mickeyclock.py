import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 1280, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load("mickeyclock.png")
minute_hand = pygame.image.load("right_hand-removebg-preview.png")
second_hand = pygame.image.load("left_hand-removebg-preview.png")

def rot_center(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()

    minute_angle = -(now.minute * 6) + 62
    second_angle = -(now.second * 6) - 62

    center_x, center_y = WIDTH // 2, HEIGHT // 2

    rotated_minute, min_rect = rot_center(minute_hand, minute_angle, (center_x, center_y))
    rotated_second, sec_rect = rot_center(second_hand, second_angle, (center_x, center_y))

    min_rect.center = (center_x, center_y)
    sec_rect.center = (center_x, center_y)

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
