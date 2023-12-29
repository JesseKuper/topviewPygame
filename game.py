import pygame

def playerMovement(playing, posX, posY, speed, north, east, south, west, walls, outside, listX, listY):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                north = True
            if event.key == pygame.K_d:
                east = True
            if event.key == pygame.K_s:
                south = True
            if event.key == pygame.K_a:
                west = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                north = False
            if event.key == pygame.K_d:
                east = False
            if event.key == pygame.K_s:
                south = False
            if event.key == pygame.K_a:
                west = False
    if not outside:
        if (posY - walls[0]) < 25:
            north = False
        if (posX - walls[1]) > - 75:
            east = False
        if (posY - walls[2]) > - 75:
            south = False
        if (posX - walls[3]) < 25:
            west = False

    #if outside:
        #if len(listX) > 0:
            #for pos in listX:
                #pass
    
    #elifs if no diagonal !!
    if north:
        posY -= speed
    if south:
        posY += speed
    if east:
        posX += speed
    if west:
        posX -= speed
    return playing, posX, posY, north, east, south, west


def playerDraw(screen, posX, posY, sizeX, sizeY):
    player = pygame.draw.rect(screen, "green", pygame.Rect(posX, posY, sizeX, sizeY))
    return player

def houseDraw(screen, screenX, screenY):
    floor = pygame.draw.rect(screen, (161, 102, 47), pygame.Rect(screenX // 10, screenY // 10, screenX - (screenX//5), screenY - (screenY//5)))

    wN = pygame.draw.rect(screen, (200, 102, 100), pygame.Rect(screenX // 10 - 20, (screenY // 10) - 20, screenX - (screenX//5) + 40, 20))
    wS = pygame.draw.rect(screen, (200, 102, 100), pygame.Rect(screenX // 10 - 20, screenY - (screenY // 10), screenX - (screenX//5) +40, 20))
    wE = pygame.draw.rect(screen, (200, 102, 100), pygame.Rect(screenX - (screenX // 10) , screenY // 10, 20, screenY - (screenY//5)))
    wW = pygame.draw.rect(screen, (200, 102, 100), pygame.Rect(screenX // 10 - 20, screenY // 10, 20, screenY - (screenY//5)))

    door = pygame.draw.rect(screen, "black", pygame.Rect(screenX - (screenX // 4), screenY - (screenY // 10) - 20, screenX//10, 40))
    
    walls = [wN.y, wE.x, wS.y, wW.x]
    return floor, walls, door

def outsideCalcMap(screen, map, mapCalcd):
    telX = 0
    telY = 0
    listX = []
    listY = []
    for i in map:
        #telY += 120
        telX = 0
        string = i.split()
        for x in string:
            #telX += 120
            if int(x) == 1:
                listX.append(telX)
                listY.append(telY)
            telX += 120
        telY += 120
    mapCalcd = True
    print("FINISH_DWADAWDADAWDADAWDAWD")
    return listX, listY, mapCalcd
        
def outsideDrawMap(screen, listX, listY):
    tel = 0
    while tel <= len(listX):
        try:
            mapBuild = pygame.draw.rect(screen, (0, 101, 168), pygame.Rect(listX[tel], listY[tel], 120, 120))
        except:
            pass # er komt error 1k in de zoveel frames idk waarom
        tel += 1


def collissions(outside, door, player, sizeX, sizeY):
    if player.colliderect(door):
        outside = True
        sizeX = 25
        sizeY = 25
    return outside, sizeX, sizeY

