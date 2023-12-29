import pygame
from game import *

pygame.init()
FPS = 60
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
dt = clock.tick(FPS)/1000
playing = True
posX = screenX //2
posY = screenY //2
sizeX = 75
sizeY = 75
north = east = south = west = False
speed = 500*dt
walls = [0,0,0,0]
outside = False
mapCalcd = False
listX = []
listY = []

map = [
    "1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1",
]



while playing:
    playing, posX, posY, north, east, south, west = playerMovement(
        playing, posX, posY, speed, north, east, south, west, walls, outside, listX, listY
        )

    
    if outside:
        screen.fill((2, 87, 24))#(0, 101, 168) als je weer water da wil
        if not mapCalcd:
            listX, listY, mapCalcd = outsideCalcMap(screen, map, mapCalcd)
        grass = outsideDrawMap(screen, listX, listY)
    elif not outside:
        screen.fill("black")
        floor, walls, door = houseDraw(screen, screenX, screenY)
    player = playerDraw(screen, posX, posY, sizeX, sizeY)
    outside, sizeX, sizeY = collissions(outside, door, player, sizeX, sizeY)
    pygame.display.flip()

    clock.tick(FPS) 

pygame.quit()
