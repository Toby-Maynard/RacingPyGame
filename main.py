import time
import math
import pygame


GRASS = pygame.image.load("imgs/grass.jpg")
TRACK = pygame.image.load("imgs/track.png")

TRACK_BOARDER = pygame.image.load("imgs/track-border.png")
FINISH = pygame.image.load("imgs/finish.png")

RED_CAR = pygame.image.load("imgs/red-car.png")
PURPLE_CAR = pygame.image.load("imgs/purple-car.png")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing game!!")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
pygame.quit()