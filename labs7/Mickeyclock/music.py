import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BG_COLOR = (40, 20, 20)
BTN_COLOR = (80, 40, 40)

play_img = pygame.image.load("playy.png")
pause_img = pygame.image.load("pause.png")
stop_img = pygame.image.load("stop.png")
next_img = pygame.image.load("next.png")
prev_img = pygame.image.load("prev.png")

btn_size = 60
play_img = pygame.transform.scale(play_img, (btn_size, btn_size))
pause_img = pygame.transform.scale(pause_img, (btn_size, btn_size))
stop_img = pygame.transform.scale(stop_img, (btn_size, btn_size))
next_img = pygame.transform.scale(next_img, (btn_size, btn_size))
prev_img = pygame.transform.scale(prev_img, (btn_size, btn_size))

center_x = WIDTH // 2
center_y = HEIGHT // 2
play_pause_rect = play_img.get_rect(center=(center_x, center_y))
stop_rect = stop_img.get_rect(center=(center_x - 120, center_y))
next_rect = next_img.get_rect(center=(center_x + 80, center_y))
prev_rect = prev_img.get_rect(center=(center_x - 80, center_y))

music_files = ["Chezile_-_Beanie_78264746.mp3", "Lady_Gaga_Bruno_Mars_-_Die_With_A_Smile_78229086.mp3", "Beach_House_-_Space_Song_73372977.mp3"]
current_track = 0
music_stopped = False
music_paused = False

def play_music(track):
    """Функция воспроизведения музыки"""
    global music_stopped, music_paused
    if os.path.exists(music_files[track]):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_files[track])
        pygame.mixer.music.play()
        music_stopped = False
        music_paused = False
        print(f"Playing: {music_files[track]}")
    else:
        print(f"Файл {music_files[track]} не найден!")

play_music(current_track)

done = False
while not done:
    screen.fill(BG_COLOR)
    
    for rect in [play_pause_rect, stop_rect, next_rect, prev_rect]:
        pygame.draw.circle(screen, BTN_COLOR, rect.center, btn_size // 2 + 10)
    
    if music_paused:
        screen.blit(play_img, play_pause_rect)  
    else:
        screen.blit(pause_img, play_pause_rect)
    
    screen.blit(stop_img, stop_rect)
    screen.blit(next_img, next_rect)
    screen.blit(prev_img, prev_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_pause_rect.collidepoint(event.pos):
                if music_stopped:
                    play_music(current_track)  
                elif music_paused:
                    pygame.mixer.music.unpause()  
                    music_paused = False
                    print("Resumed")
                else:
                    pygame.mixer.music.pause()  
                    music_paused = True
                    print("Paused")
            elif stop_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()
                music_stopped = True
                print("Stopped")
            elif next_rect.collidepoint(event.pos):
                current_track = (current_track + 1) % len(music_files)
                play_music(current_track)
            elif prev_rect.collidepoint(event.pos):
                current_track = (current_track - 1) % len(music_files)
                play_music(current_track)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if music_stopped:
                    play_music(current_track)
                elif music_paused:
                    pygame.mixer.music.unpause()
                    music_paused = False
                    print("Resumed")
                else:
                    pygame.mixer.music.pause()
                    music_paused = True
                    print("Paused")
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
                music_stopped = True
                print("Stopped")
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                play_music(current_track)
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                play_music(current_track)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
