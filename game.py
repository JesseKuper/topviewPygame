import pygame

def HUD(screen, screenX, screenY, coins):
    #font = pygame.font.SysFont(None, 60)
    #img = font.render(f"Coins: {coins}", True, "black")
    #screen.blit(img, (20, 20))
    return coins

def playerMovement(playing, posX, posY, speed, north, east, south, west, walls, outside, listX, listY, sizeX, sizeY, FPS, lastLoc, inwater, dt, attack, use, shopSel):
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
            if event.key == pygame.K_SPACE:
                attack = True
            if event.key == pygame.K_e:
                use = True
            if event.key == pygame.K_DOWN:
                if shopSel < 2:
                    shopSel += 1
            if event.key == pygame.K_UP:
                if shopSel > 0:
                    shopSel -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                north = False
            if event.key == pygame.K_d:
                east = False
            if event.key == pygame.K_s:
                south = False
            if event.key == pygame.K_a:
                west = False
            if event.key == pygame.K_SPACE:
                attack = False

    if not outside:
        if (posY - walls[0]) < 25:
            north = False
        if (posX - walls[1]) > - 75:
            east = False
        if (posY - walls[2]) > - 75:
            south = False
        if (posX - walls[3]) < 25:
            west = False

    if outside: 
        if posX < 0: #SCREENX ENZ Niet VARIABLE
            posX += speed*1.2
        if posY < 0:
            posY += speed*1.2
        if posY > 1055:
            posY -= speed*1.2
        if posX > 1895:
            posX -= speed*1.2
            
        postel = 0
        fpstel = 0
        if len(listX) > 0:
            while postel <= len(listX): 
                try: 
                    if posX >= listX[postel] and posX <= listX[postel] + 60 and posY >= listY[postel] and posY <= listY[postel] + 60:
                        inwater = True
                except:
                    pass #fix dit
                postel += 1
            if not inwater:
                speed = 250*dt
            if inwater:
                speed = 70*dt
                inwater = False

                
                
    
    #elifs if no diagonal !!
    if north:
        posY -= speed
    if south:
        posY += speed
    if east:
        posX += speed
    if west:
        posX -= speed
    return playing, posX, posY, north, east, south, west, lastLoc, inwater, speed, attack, use, shopSel





def playerDraw(screen, posX, posY, sizeX, sizeY, outside, attack, health, mana, screenX, screenY):
    if outside and attack: 
        borderFill = pygame.draw.rect(screen, (161, 5, 33), pygame.Rect(posX -50, posY -  50, 125, 125 ))
        borderN = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX -50, posY -  50, 125, 5 ))
        borderS = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX -50, posY +  70, 125, 5 ))
        borderW = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX - 50, posY - 50, 5, 125 ))
        borderE = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX + 70, posY - 50, 5, 125 ))
    
    player = pygame.draw.rect(screen, "white", pygame.Rect(posX, posY, sizeX, sizeY))
    playerCol = pygame.draw.rect(screen, (47, 60, 77), pygame.Rect(posX+ 5, posY+ 5, sizeX-10, sizeY-10))

    healthEmpty = pygame.draw.rect(screen, (156, 156, 156), pygame.Rect(screenX//2 - 255, screenY - 85, 510, 30))
    healthMeter = pygame.draw.rect(screen, "red", pygame.Rect(screenX//2 - 250, screenY - 80, health*5, 20))

    manaEmpty = pygame.draw.rect(screen, (156, 156, 156), pygame.Rect(screenX//2 - 255, screenY - 45, 510, 30))
    manaMeter = pygame.draw.rect(screen, "blue", pygame.Rect(screenX//2 - 250, screenY - 40, mana*5, 20))
    return player




def houseDraw(screen, screenX, screenY):
    floor = pygame.draw.rect(screen, (161, 102, 47), pygame.Rect(screenX // 10, screenY // 10, screenX - (screenX//5), screenY - (screenY//5)))

    wN = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenX // 10 - 20, (screenY // 10) - 20, screenX - (screenX//5) + 40, 20))
    wS = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenX // 10 - 20, screenY - (screenY // 10), screenX - (screenX//5) +40, 20))
    wE = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenX - (screenX // 10) , screenY // 10, 20, screenY - (screenY//5)))
    wW = pygame.draw.rect(screen, (200, 200, 100), pygame.Rect(screenX // 10 - 20, screenY // 10, 20, screenY - (screenY//5)))

    door = pygame.draw.rect(screen, "black", pygame.Rect(screenX - (screenX // 4), screenY - (screenY // 10) - 20, screenX//10, 40))
    
    walls = [wN.y, wE.x, wS.y, wW.x]
    return floor, walls, door

def armoryDraw(screen, screenX, screenY):
    floor = pygame.draw.rect(screen, (153, 153, 153), pygame.Rect(screenX // 10- 20, (screenY // 10) - 20, screenX / 3, screenY - (screenY//5) + 20))
 
    wN = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect(screenX // 10- 20, (screenY // 10) - 20, screenX // 3 + 20, 20))
    wS = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect(screenX // 10 - 20, screenY - (screenY // 10), screenX // 3 + 20, 20))
    wE = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect((screenX // 2) - 150 , screenY // 10, 20, screenY - (screenY//5)))
    wW = pygame.draw.rect(screen, (56, 56, 56), pygame.Rect(screenX // 10 - 20, screenY // 10, 20, screenY - (screenY//5)))

    shop = pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(300, 200, 400, 100))

    door = pygame.draw.rect(screen, "black", pygame.Rect(screenX // 3 + 150, screenY - (screenY//3), 40, 150))
    
    walls = [wN.y, wE.x, wS.y, wW.x]
    return floor, walls, door, shop.y

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
            telX += 60
        telY += 60
    mapCalcd = True
    print("FINISH_DWADAWDADAWDADAWDAWD")
    return listX, listY, mapCalcd
        
def outsideDrawMap(screen, listX, listY):
    tel = 0
    while tel <= len(listX):
        try:
            mapBuild = pygame.draw.rect(screen, (0, 101, 168), pygame.Rect(listX[tel], listY[tel], 60, 60))
        except:
            pass # er komt error 1k in de zoveel frames idk waarom
        tel += 1

def outsideDraw(screen, screenX, screenY):
    width = 0
    house = pygame.draw.rect(screen, "red", pygame.Rect(200, 100, 300, 200))
    houseEntrance = pygame.draw.rect(screen, "black", pygame.Rect(310, 290, 80, 20))

    armory = pygame.draw.rect(screen, (46, 46, 46), pygame.Rect(400, screenY - 250, 120, 220))
    armoryEntrance = pygame.draw.rect(screen, "black", pygame.Rect(515, screenY - 90, 15, 40))

    return houseEntrance, armoryEntrance

def shopMenu(screen, screenX, screenY, shopSel):
    cost = 0
    backgroundBorder = pygame.draw.rect(screen, (219, 172, 52), pygame.Rect(screenX - (screenX // 2), (screenY // 10) - 20, screenX / 3 + 150, screenY - (screenY//5) + 20))
    background = pygame.draw.rect(screen, (153, 153, 153), pygame.Rect(screenX - (screenX // 2)+ 20, (screenY // 10), screenX / 3 + 110, screenY - (screenY//5) -20))
    c1=c2=c3= (100, 100, 100)
    if shopSel == 0:
        cost = 50
        c1 = (150, 150, 150)
        wbY = (screenY // 10) + 10
    elif shopSel == 1:
        cost = 100
        c2 = (150, 150, 150)
        wbY = (screenY // 10) + 245
    elif shopSel == 2:  
        cost = 200
        c3 = (150, 150, 150)
        wbY = (screenY // 10) + 480
    windowBackground = pygame.draw.rect(screen, (219, 172, 52), pygame.Rect(screenX - (screenX // 2)+ 30, wbY, screenX / 3 + 90, (screenY//5) + 20 ))

    window1 = pygame.draw.rect(screen, c1, pygame.Rect(screenX - (screenX // 2)+ 40, (screenY // 10)+ 20, screenX / 3 + 70, screenY//5))
    image1Load = pygame.image.load("images/example.png") ### maak images 285 bij 170
    image1 = pygame.draw.rect(screen, "white", pygame.Rect(1400, 150, 285, 170))
    screen.blit(image1Load, image1)
    font = pygame.font.SysFont(None, 30)
    pName = font.render("PRODDUCT NAME", True, "white")
    screen.blit(pName, (screenX - (screenX // 2)+ 50, (screenY // 10)+ 40))

    font = pygame.font.SysFont(None, 25)
    pStat1 = font.render("- STAT NUMBER 1", True, "white")
    screen.blit(pStat1, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 90))
    font = pygame.font.SysFont(None, 25)
    pStat2 = font.render("- STAT NUMBER 2", True, "white")
    screen.blit(pStat2, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 120))
    font = pygame.font.SysFont(None, 25)
    pStat3 = font.render("- STAT NUMBER 3", True, "white")
    screen.blit(pStat3, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 150))
    font = pygame.font.SysFont(None, 25)
    pStat4 = font.render("- STAT NUMBER 4", True, "white")
    screen.blit(pStat4, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 180))


    window2 = pygame.draw.rect(screen, c2, pygame.Rect(screenX - (screenX // 2)+ 40, (screenY // 10)+(screenY//5 ) + 40, screenX / 3 + 70, (screenY//5)))
    image2Load = pygame.image.load("images/example.png") ### maak images 285 bij 170
    image2 = pygame.draw.rect(screen, "white", pygame.Rect(1400, 170+(screenY//5 ), 285, (screenY//5 ) - 40))
    screen.blit(image2Load, image2)
    font = pygame.font.SysFont(None, 30)
    p2Name = font.render("PRODDUCT NAME", True, "white")
    screen.blit(p2Name, (screenX - (screenX // 2)+ 50, (screenY // 10)+ 60+(screenY//5 )))

    font = pygame.font.SysFont(None, 25)
    p2Stat1 = font.render("- STAT NUMBER 1", True, "white")
    screen.blit(p2Stat1, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 110+(screenY//5 )))
    font = pygame.font.SysFont(None, 25)
    p2Stat2 = font.render("- STAT NUMBER 2", True, "white")
    screen.blit(p2Stat2, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 140+(screenY//5 )))
    font = pygame.font.SysFont(None, 25)
    p2Stat3 = font.render("- STAT NUMBER 3", True, "white")
    screen.blit(p2Stat3, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 170+(screenY//5 )))
    font = pygame.font.SysFont(None, 25)
    p2Stat4 = font.render("- STAT NUMBER 4", True, "white")
    screen.blit(p2Stat4, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 200+(screenY//5 )))



    window3 = pygame.draw.rect(screen, c3, pygame.Rect(screenX - (screenX // 2)+ 40, (screenY // 10)+(screenY//5) + 275, screenX / 3 + 70, (screenY//5)))
    image3Load = pygame.image.load("images/example.png") ### maak images 285 bij 170
    image3 = pygame.draw.rect(screen, "white", pygame.Rect(1400, 405+(screenY//5 ), 285, (screenY//5 ) - 40))
    screen.blit(image3Load, image3)
    font = pygame.font.SysFont(None, 30)
    p3Name = font.render("PRODDUCT NAME", True, "white")
    screen.blit(p3Name, (screenX - (screenX // 2)+ 50, (screenY // 10)+ 295+(screenY//5 )))

    font = pygame.font.SysFont(None, 25)
    p3Stat1 = font.render("- STAT NUMBER 1", True, "white")
    screen.blit(p3Stat1, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 345+(screenY//5 )))
    font = pygame.font.SysFont(None, 25)
    p3Stat2 = font.render("- STAT NUMBER 2", True, "white")
    screen.blit(p3Stat2, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 375+(screenY//5 )))
    font = pygame.font.SysFont(None, 25)
    p3Stat3 = font.render("- STAT NUMBER 3", True, "white")
    screen.blit(p3Stat3, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 405+(screenY//5 )))
    font = pygame.font.SysFont(None, 25)
    p3Stat4 = font.render("- STAT NUMBER 4", True, "white")
    screen.blit(p3Stat4, (screenX - (screenX // 2)+ 70, (screenY // 10)+ 435+(screenY//5 )))

    font = pygame.font.SysFont(None, 40)
    nav1 = font.render("arrow Up / down", True, "white")
    screen.blit(nav1, (screenX - (screenX // 2)+ 50, (screenY // 10)+ 500+(screenY//5 )))

    font = pygame.font.SysFont(None, 40)
    nav1 = font.render("Enter to selects", True, "white")
    screen.blit(nav1, (screenX - (screenX // 2)+ 50, (screenY // 10)+ 550+(screenY//5 )))
    
    font = pygame.font.SysFont(None, 80)
    nav1 = font.render(f"cost: {cost}", True, "white")
    screen.blit(nav1, (screenX - (screenX // 2)+ 520, (screenY // 10)+ 525+(screenY//5 )))


def collissions(screen, outside, house, armory, door, player, sizeX, sizeY, houseEntrance, armoryEntrance, dt, speed, posX, posY, shop, use, screenX, screenY, shopSel):
    if outside:
        if player.colliderect(houseEntrance):
            house = True
            armory = False
            outside = False
            speed = 400*dt
            sizeX = 75
            sizeY = 75
            posX = 1520
            posY = 840
        elif player.colliderect(armoryEntrance):
            house = False
            armory = True
            outside = False
            speed = 400*dt
            sizeX = 75
            sizeY = 75
            posX = 680
            posY = 770
    if not outside:
        if player.colliderect(door):
            if armory:
                posX = 560
                posY = 990
            elif house:
                posX = 350
                posY = 330
            armory = False
            house = False
            outside = True
            speed = 250*dt
            sizeX = 25
            sizeY = 25
        if armory:
            if posY - shop < 200:
                if not use:
                    font = pygame.font.SysFont(None, 30)
                    img = font.render("SHOP (E)", True, "white")
                    screen.blit(img, (posX + 80, posY - 20))
                if use:
                    shopMenu(screen, screenX, screenY, shopSel)
            else:
                use = False
    return outside, house, armory, sizeX, sizeY, speed, posX, posY, use


exec(open("main.py").read())#### WEGHALEN IS VOOR TESTEN ZODAT F5 KAN DOEN IN DIT BESTAND
    
