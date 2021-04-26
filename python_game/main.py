# importing pygame

import pygame
import random
import math

from pygame import mixer
                                                                                    # initializing pygame
pygame.init()
                                                                                    # set display size
screen = pygame.display.set_mode((800, 600))
                                                                                    # adding display caption of our game
pygame.display.set_caption("Space Warrior")
icon = pygame.image.load('ship.png')                                                # loading and adding icon of our game
pygame.display.set_icon(icon)
background = pygame.image.load('sky.jpg')

mixer.music.load('play.mp3')
mixer.music.play(-1)

playerimg = pygame.image.load('player.png')                                         # adding player image and its position
playerX = 360
playerY = 480
playerX_change = 0
playerY_change =0
explosionimg = pygame.image.load('explosion.png')

enemyimg = []
enemyX = []                                                   # enemy and enemy_bullet addition
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 4


enbulletimg=[]
enbulletY_change=1
enbulletY=[]
enbulletX=[]

for i in range(num_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))                                # adding enemy image and its position
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 100))
    enemyX_change.append(3)
    enemyY_change.append(40)


    enbulletimg.append(pygame.image.load('enbullet.png'))                         #enemy bullet firing
    enbulletX.append(enemyX[i])
    enbulletY.append(enemyY[i])




bulletimg = pygame.image.load('bullet.png')                                        # adding bullet image and its position
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

over_font = pygame.font.Font('freesansbold.ttf', 64)





def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (250, 300))


def show_score(X, Y):
    score = font.render("Score : " + str(score_value), True, (50, 0, 255))
    screen.blit(score, (X, Y))


def player(X, Y):
    screen.blit(playerimg, (X, Y))


def enemy(X, Y, i):
    screen.blit(enemyimg[i], (X, Y))


def enemy_bullet(X, Y,i):                                               #enemy bullet  function
    screen.blit(enbulletimg[i], (X, Y))



def fire_bullet(X, Y):                                                    # firing bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (X + 42, Y + 10))

def ship_collision(playerX,playerY,enbulletX,enbulletY):
    c_distance = math.sqrt(math.pow((playerX - 10) - enbulletX[i], 2) + math.pow(playerY - enbulletY[i], 2))
    if c_distance < 40:
        return True
    else:
        return False
                                                                               # collosion of enemy and bullet
def iscollision(enemyX, enemyY, bulletX, bulletY):

    distance = math.sqrt(math.pow((enemyX - 10) - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 30:
        return True
    else:
        return False
                                                                             #enemy ship collision
def ship_enemy_collision(enemyY,enemyX,playerX,playerY):
    s_distance = math.sqrt(math.pow((enemyX - 10) - playerX, 2) + math.pow(enemyY - playerY, 2))
    if s_distance < 30:
        return True
    else:
        return False

def explosion(X, Y, i):
    screen.blit(explosionimg, (X, Y))


running = True
while running:
    # RGB - Red Green Blue          screen filling

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():                                             # for open and closing game event
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:                                        # for player movement
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_UP:                                        # for player movement
                playerY_change = -4

            if event.key == pygame.K_DOWN:
                playerY_change = 4

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerY+=playerY_change
    playerX += playerX_change

    if playerY <= 0:
        playerY = 0                                                                   # changing positio of player and set limit under display resolution
    if playerY >= 500:
        playerY = 500

    if playerX <= 0:
        playerX = 0                                                                   # changing positio of player and set limit under display resolution
    if playerX >= 672:
        playerX = 672

    for i in range(num_enemies):


        shipcollision=ship_collision(playerX,playerY,enbulletX,enbulletY)
        if shipcollision is True:                                                         #ship collision
            bullet_sound=mixer.Sound("explosion.wav")
            bullet_sound.play()
            for j in range(num_enemies):
                enemyY[j] = 2000
            playerimg=explosionimg
            game_over_text()
            break
        enemy_and_ship_collision=ship_enemy_collision(enemyY[i],enemyX[i],playerX,playerY)
        if enemy_and_ship_collision is True:
            bullet_sound=mixer.Sound("explosion.wav")
            bullet_sound.play()
            for j in range(num_enemies):
                enemyY[j] = 2000
            playerimg=explosionimg
            game_over_text()
            break

        if enemyY[i] > 430:
            for j in range(num_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]                                             # changing position of enemy and set limit under display resolution
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]


        enbulletY[i]+=enbulletY_change                                                #enemy bullet fire
        if enbulletY[i]>550:
            enbulletY[i]=enemyY[i]
            enbulletY[i]+=enbulletY_change
        enemy_bullet(enbulletX[i],enbulletY[i],i)



        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_sound=mixer.Sound("explosion.wav")
            bullet_sound.play()
            explosion(enemyX[i], enemyY[i], i)
            bullet_state = "ready"
            bulletY = playerY
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 100)
        enemy(enemyX[i], enemyY[i], i)


    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(10, 10)
    pygame.display.update()
