import pygame
from town import *
from wild import *


#### To Do
#MagicHouse
#wild
# hud
#chests
# Spritesssss ## misschien als blokjes er goed uit ziet ist ook goed
###Nog niet aan toe, eerst aaasprites
### bomen in map late toevoege met 3??// pad ook met 4 fz


#abilityte ideen:
    #shield maar groter en alleen outline geeft slow


pygame.init()
FPS = 60
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
dt = clock.tick(FPS)/1000
playing = False
menu = True
paused = False
inv = False
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
list2X = []
list2Y = []
lastLoc = []
inwater = False
houseEntrance = 0
armoryEntrance = 0
wildEntrance = 0
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
directionX = "north"
directionY = "west"
mb1Attack = False
enemy1 = ""
e1posX = 1700
e1posY = 800
e1Health = 30
invItems = []
wild = False
pausemen = False

#items:
    #blocky_blood

map = [ ## oude grid
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
    "0 0 0 0 0 0 0 0 0 0 2 2 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 1 1 1",
    "0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1",
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
    selected, playTextWidth, menu, playing = startMenu(screen, screenX, screenY, selected, playTextWidth, menu, playing)
    pygame.display.flip()

    clock.tick(FPS) 







while playing:
    coins = HUD(screen, screenX, screenY, coins) # bestaat nog niet doet nu niks
    playing, posX, posY, north, east, south, west, lastLoc, inwater, speed, attack, use, shopSel, mb1Attack, inv, pausemen = playerMovement(playing, posX, posY, speed, north, east, south, west, walls, outside, listX, listY, sizeX, sizeY, FPS, lastLoc, inwater, dt, attack, use, shopSel, mb1Attack, inv, paused, pausemen) ## PLAYER MOVEMENT VERDELEN Dit is te groot later doen
    directionX, directionY, mX, mY = playerLookDirection(posX, posY, directionX, directionY)### DOet op het moment Niks maar checkt waar muis is en geeft door of je links/ rechts/ boven enz bent van speler
    if wild:
        
        screen.fill((2, 87, 24))#(0, 101, 168) als je weer water da wil
        if not mapCalcd:
            map = newMap()
            listX, listY, list2X, list2Y, mapCalcd = outsideCalcMap(screen, map, mapCalcd)
        grass = outsideDrawMap(screen, listX, listY, list2X, list2Y)
        wildEntrance = wildDraw(screen, screenX, screenY)
        enemy1, e1posX, e1posY, e1Health, invItems = enemy(screen, posX, posY, outside, e1posX, e1posY, e1Health, paused, invItems, player, enemy1)


    if outside and not wild:
        screen.fill((2, 87, 24))#(0, 101, 168) als je weer water da wil
        if not mapCalcd:
            listX, listY, list2X, list2Y, mapCalcd = outsideCalcMap(screen, map, mapCalcd)
        grass = outsideDrawMap(screen, listX, listY, list2X, list2Y)
        houseEntrance, armoryEntrance, wildEntrance = outsideDraw(screen, screenX, screenY)
        

    elif not outside:
        if house:
            screen.fill("black")
            floor, walls, door = houseDraw(screen, screenX, screenY)
        if armory:
            screen.fill("black")
            floor, walls, door, shop = armoryDraw(screen, screenX, screenY)

    player, mana, shield = playerDraw(screen, posX, posY, sizeX, sizeY, outside, attack, health, mana,  screenX, screenY, paused)

    ###WERKT NIETmb1Attack = playerWeapons(mb1Attack, screen, posX, posY, mX, mY, sizeX, sizeY, directionX, directionY)

    outside, house, armory, sizeX, sizeY, speed, posX, posY, use, health, e1Health, wild, mapCalcd, playing, menu = collissions(screen, outside, house, armory, door, player, sizeX, sizeY, houseEntrance, armoryEntrance, wildEntrance, dt, speed, posX, posY, shop, use, screenX, screenY, shopSel, enemy1, health, e1Health, shield, paused, wild, mapCalcd, playing, menu)
    if inv:
        paused = True
        inventory(screen, screenX, screenY, invItems)
    else:
        paused = False

    if pausemen:
        paused = True
        pausemen, playing, menu = pauseMenu(screen, screenX, screenY, mb1Attack, pausemen, playing, menu)
    else:
        paused = False
    
    pygame.display.flip()

    clock.tick(FPS) 

pygame.quit()
