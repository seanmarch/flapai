import sys

import pygame

pygame.init()

WINDOW = (640, 480)

SCORE = 0

BIRD_Y = 240
BIRD_X = 100

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

BIRD_RADIUS = 20
BIRD_LINE_WIDTH = 0

REC_WIDTH = 50
REC_HEIGHT = 150
REC1_X = 640
REC1_Y = 330
REC2_X = 640
REC2_Y = 0

font = pygame.font.Font('freesansbold.ttf', 32)


def gravity(y):
    y += 0.2
    return y


def jump(y):
    y -= 40
    return y


def move_pipes(REC1_X, REC2_X):
    REC1_X -= 0.5
    REC2_X -= 0.5
    return REC1_X, REC2_X


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
        if event.type == pygame.KEYUP:
            BIRD_Y = jump(BIRD_Y)

    screen = pygame.display.set_mode(WINDOW)
    screen.fill(BLUE)

    if BIRD_Y < 460:
        BIRD_Y = gravity(BIRD_Y)

    if REC1_X == -50:
        REC1_X = 640
        REC2_X = 640
        SCORE += 1

    circle = pygame.draw.circle(screen, WHITE, (BIRD_X, int(BIRD_Y)), BIRD_RADIUS, BIRD_LINE_WIDTH)

    rectangle1 = pygame.draw.rect(screen, GREEN, (REC1_X, REC1_Y, REC_WIDTH, REC_HEIGHT), BIRD_LINE_WIDTH)
    rectangle2 = pygame.draw.rect(screen, GREEN, (REC2_X, REC2_Y, REC_WIDTH, REC_HEIGHT), BIRD_LINE_WIDTH)

    text = font.render('Score: ' + str(SCORE), True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.center = (320, 240)
    screen.blit(text, textRect)

    REC1_X, REC2_X = move_pipes(REC1_X, REC2_X)

    pygame.display.update()
