import pygame
from game import *


pygame.init()
FPS = 60
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
dt = clock.tick(FPS)/1000
playing = False
menu = True
posX = 250
posY = 150
sizeX = 75
sizeY = 75
north = east = south = west = False
speed = 400*dt
walls = [0,0,0,0]
outside = False
mapCalcd = False
listX = []
listY = [] # hier miss dict van maken als zin in hebt nu ni :)
lastLoc = []
inwater = False
houseEntrance = 0
armoryEntrance = 0
house = True
armory = False
coins = 0
health = 100
mana = 50
attack = False
shop = 0
use = False
shopSel = 0
selected = 3
playTextWidth = 0

map = [
    "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1",
]
map = [
    "1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
    "1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
]


while menu:
    screen.fill("white")
    selected, playTextWidth = startMenu(screen, screenX, screenY, selected, playTextWidth)
    pygame.display.flip()

    clock.tick(FPS) 







while playing:
    coins = HUD(screen, screenX, screenY, coins) # bestaat nog niet doet nu niks
    playing, posX, posY, north, east, south, west, lastLoc, inwater, speed, attack, use, shopSel = playerMovement(
        playing, posX, posY, speed, north, east, south, west, walls, outside, listX, listY, 
        sizeX, sizeY, FPS, lastLoc, inwater, dt, attack, use, shopSel) ## PLAYER MOVEMENT VERDELEN Dit is te groot later doen

    
    
    if outside:
        screen.fill((2, 87, 24))#(0, 101, 168) als je weer water da wil
        if not mapCalcd:
            listX, listY, mapCalcd = outsideCalcMap(screen, map, mapCalcd)
        grass = outsideDrawMap(screen, listX, listY)
        houseEntrance, armoryEntrance = outsideDraw(screen, screenX, screenY)

    elif not outside:
        if house:
            screen.fill("black")
            floor, walls, door = houseDraw(screen, screenX, screenY)
        if armory:
            screen.fill("black")
            floor, walls, door, shop = armoryDraw(screen, screenX, screenY)

    player = playerDraw(screen, posX, posY, sizeX, sizeY, outside, attack, health, mana,  screenX, screenY)

    outside, house, armory, sizeX, sizeY, speed, posX, posY, use = collissions(
        screen, outside, house, armory, door, player, sizeX, sizeY, 
        houseEntrance, armoryEntrance, dt, speed, posX, posY, shop, use,
        screenX, screenY, shopSel)
    
    pygame.display.flip()

    clock.tick(FPS) 

pygame.quit()
