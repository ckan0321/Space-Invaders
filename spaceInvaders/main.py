import pygame
import random

# Initialize game and screen
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player icon
playerImg = pygame.image.load("spaceship.png")
playerX = 368
playerY = 450
playerX_change = 0
score = 0

# Generate enemies
enemyImg = pygame.image.load("enemy.png")
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = 40
enemyNum = 6
for i in range(enemyNum):
    enemyX.append(random.randint(0, 768))
    enemyY.append(random.randint(20 * i, 20 * i + 80))
    enemyX_change.append(0.3)
# Bullet icon
bulletImg = pygame.image.load("bullet.png")
bulletX = playerX + 16
bulletY = playerY + 10
bulletY_change = 0.5
bullet_state = "ready"

# Background
background = pygame.image.load("BackgroundSpace.jpeg")


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Checks for movement keystrokes
        key_down_event_list = pygame.key.get_pressed()
        if key_down_event_list[pygame.K_LEFT] and key_down_event_list[pygame.K_RIGHT]:
            playerX_change = 0
        elif key_down_event_list[pygame.K_RIGHT]:
            playerX_change = 0.6
        elif key_down_event_list[pygame.K_LEFT]:
            playerX_change = -0.6
        elif not key_down_event_list[pygame.K_LEFT] and not key_down_event_list[pygame.K_RIGHT]:
            playerX_change = 0
        # Check for bullet firing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX + 16
                fire_bullet(bulletX, bulletY)

    screen.fill((140, 79, 243))

    # Background
    screen.blit(background, (0, 0))

    # Player Bounds
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736

    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Enemy Movement
    for i in range(enemyNum):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= 784:
            enemyX_change[i] *= -1
            enemyX[i] += enemyX_change[i]
            enemyY[i] += enemyY_change
        # Collision Detection
        if abs(bulletX - enemyX[i]) < 24 and abs(bulletY - enemyY[i]) < 4:
            bullet_state = "ready"
            bulletY = playerY
            enemyX[i] = random.randint(0, 784)
            enemyY[i] = random.randint(0, 284)
            score += 1
            print(score)
        enemy(enemyX[i], enemyY[i])

    player(playerX, playerY)
    pygame.display.update()
