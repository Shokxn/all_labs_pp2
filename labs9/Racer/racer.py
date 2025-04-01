import pygame, sys, random, time
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Настройки FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Константы экрана и игры
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 650
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
RECORD = 0
COINS_FOR_SPEEDUP = 5  # Количество монет для увеличения скорости врага

# Настройки шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
restart_text = font_small.render("Press R to Restart or Q to Quit", True, BLACK)

# Загрузка фона и музыки
background = pygame.image.load("Track.png")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

# Инициализация окна
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(200, 640), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(200, 640), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 150 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < 700 and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Класс монеты с разными весами
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.value = random.choice([1, 2, 3])  # Вес монеты
        self.respawn()

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(200, 640), random.randint(50, 500))
        self.value = random.choice([1, 2, 3])

# Функция сброса игры

def reset_game():
    global SCORE, COINS_COLLECTED, SPEED, P1, E1, C1, all_sprites, enemies, coins, RECORD
    if SCORE > RECORD:
        RECORD = SCORE
    SCORE = 0
    COINS_COLLECTED = 0
    SPEED = 5
    P1 = Player()
    E1 = Enemy()
    C1 = Coin()
    
    coins = pygame.sprite.Group()
    coins.add(C1)
    
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(C1, P1, E1)

reset_game()

# Событие увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                reset_game()
            if event.key == K_q:
                pygame.quit()
                sys.exit()
    
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    record_text = font_small.render(f"Record: {RECORD}", True, BLACK)
    
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 150, 10))
    DISPLAYSURF.blit(record_text, (SCREEN_WIDTH - 150, 40))
    
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    # Проверка на сбор монеты
    collected_coin = pygame.sprite.spritecollideany(P1, coins)
    if collected_coin:
        COINS_COLLECTED += collected_coin.value
        collected_coin.respawn()
        
        # Увеличение скорости врага после сбора N монет
        if COINS_COLLECTED % COINS_FOR_SPEEDUP == 0:
            SPEED += 1
    
    # Проверка на столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        
        DISPLAYSURF.fill(RED)
        game_over_rect = game_over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        DISPLAYSURF.blit(game_over, game_over_rect)
        DISPLAYSURF.blit(restart_text, restart_rect)
        pygame.display.update()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        waiting = False
                        reset_game()
                    if event.key == K_q:
                        pygame.quit()
                        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
q