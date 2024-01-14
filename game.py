import pygame
import random


def startMenu(screen, screenX, screenY, selected, playTextWidth, menu, playing):
    
    mx, my=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected == 0:
                playing = True
                menu = False
            elif selected == 1:
                exit()
    
    playColor = exitColor = "black"

    startPlayX = startExitX = 50
    startPlayXcol = startExitXcol = 50
    startPlayY = screenX/4 - 250
    startExitY = startPlayY + 200
    textSize = 250
    
    font = pygame.font.SysFont(None, textSize)
    playTextWidth, playTextHeight = font.size("PLAY")
    
    if selected == 0:
        playColor = "grey"
        startPlayX += 100

    elif selected == 1:
        exitColor = "grey"
        startExitX += 100


    font = pygame.font.SysFont(None, textSize)
    img = font.render("PLAY", True, playColor)
    screen.blit(img, (startPlayX, startPlayY))

    font = pygame.font.SysFont(None, textSize)
    img = font.render("EXIT", True, exitColor)
    screen.blit(img, (startExitX, startExitY))

    if mx > startPlayXcol and mx < startPlayXcol + playTextWidth and my > startPlayY and my < startPlayY + playTextHeight:
        selected = 0
    elif mx > startExitXcol and mx < startExitXcol + playTextWidth and my > startExitY and my < startExitY + playTextHeight:
        selected = 1
    else: selected = 3
    
    

    return selected, playTextWidth, menu, playing


def HUD(screen, screenX, screenY, coins): ### WRM hier niet health en mana bar!!!!!!!!!!!!!!!!!!
    #font = pygame.font.SysFont(None, 60)
    #img = font.render(f"Coins: {coins}", True, "black")
    #screen.blit(img, (20, 20))
    return coins

def playerLookDirection(posX, posY, directionX, directionY):
    mX, mY =pygame.mouse.get_pos()
    if mY - posY > 0:
        directionY = "south"
    else:
        directionY = "north"

    if mX - posX > 0:
        directionX = "east"
    else:
        directionX = "west"
    return directionX, directionY, mX, mY



######################DOET NIKS NU ---- POGING tot een magic beam fz van speler naar muis cursor
def playerWeapons(mb1Attack, screen, posX, posY, mX, mY, sizeX, sizeY, directionX, directionY):############ WERKT NOG niet later beter bekijken
    XhoekA = YhoekA =XhoekB = YhoekB =XhoekC = YhoekC =XhoekD = YhoekD =  0
    posX = posX + (sizeX/2) # de punten rood zien verkeerd uit maar ecte punt is eigelijk links boven!
    posY = posY + (sizeY/2) 
    NEmX = mX -960
    NEmY = mY
    angleX = NEmX / 5.3333
    angleY = NEmY / 5.3333

    
    if directionX == "east" and directionY == "north":
        XhoekA = mX - angleX
        YhoekA = mY - angleY

        XhoekB = mX + angleX
        YhoekB = mY + angleY

        XhoekD = posX
        YhoekD = posY - 90

        XhoekC = posX + 90
        YhoekC = posY 

    
    pos = pygame.draw.rect(screen, "red", pygame.Rect(posX, posY, 10, 10))
    Mouse = pygame.draw.rect(screen, "red", pygame.Rect(mX, mY, 10, 10))

    hoekA = pygame.draw.rect(screen, "purple", pygame.Rect(XhoekA, YhoekA, 10, 10))
    hoekB = pygame.draw.rect(screen, "purple", pygame.Rect(XhoekB, YhoekB, 10, 10))
    hoekC = pygame.draw.rect(screen, "purple", pygame.Rect(XhoekC, YhoekC, 10, 10))
    hoekD = pygame.draw.rect(screen, "purple", pygame.Rect(XhoekD, YhoekD, 10, 10))

    #particleCount = random.randint(1, 20)
    #particleSize = random.randint(10, 50)
    #particleX = random.randint(200, 500)
    #particleY = random.randint(200, 500)
    #tel = 0
    #if mb1Attack:
        #while tel < particleCount:
            #magicAttack = pygame.draw.rect(screen, "purple", pygame.Rect(particleX, particleY, particleSize, particleSize))
            #tel+= 1
    
    return mb1Attack

def playerMovement(playing, posX, posY, speed, north, east, south, west, walls, outside, listX, listY, sizeX, sizeY, FPS, lastLoc, inwater, dt, attack, use, shopSel, mb1Attack, inv, paused):
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
            if event.key == pygame.K_TAB:
                if inv:
                    inv = False
                else:
                    inv = True

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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mb1Attack = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            mb1Attack = False

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
        if posX < 0: #SCREENX ENZ Niet VARIABLE (ik snap niet wat ik hiermee bedoelde)
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
    if not paused:
        if north:
            posY -= speed
        if south:
            posY += speed
        if east:
            posX += speed
        if west:
            posX -= speed
    return playing, posX, posY, north, east, south, west, lastLoc, inwater, speed, attack, use, shopSel, mb1Attack, inv

def drops(screen, whatdrop, eposX, eposY, invItems, player, enemy1):
    if whatdrop == "blocky_blood":
        blocky_blood_sprite = pygame.image.load("images/blocky_blood.png")
        blocky_blood = pygame.draw.rect(screen, (2, 87, 24), pygame.Rect(eposX, eposY,  25, 25 ))      
        screen.blit(blocky_blood_sprite, blocky_blood)
    if player.colliderect(blocky_blood):
        invItems.append(whatdrop)
        enemy1 = "deleted"
    return invItems, enemy1

        


def inventory(screen, screenX, screenY, invItems):
    invBorder = pygame.draw.rect(screen, "black", pygame.Rect(400 - 10,100 - 10, screenX - 800 + 20, screenY - 200 + 20 ))
    invBackground = pygame.draw.rect(screen, "grey", pygame.Rect(400,100, screenX - 800, screenY - 200 ))
    textX = 400
    textY = 100
    for i in invItems:
        font = pygame.font.SysFont(None, 50)
        img = font.render(f"{i}", True, "white")
        screen.blit(img, (textX, textY))
        textX += 224
        textY += 176
    
    #112X
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,286, screenX - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,463, screenX - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,639, screenX - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,815, screenX - 800, 10 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(400,991, screenX - 800, 10 ))
    

    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(624,100, 10, screenY - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(848,100, 10, screenY - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(1072,100, 10, screenY - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(1296,100, 10, screenY - 200 ))
    invgrid = pygame.draw.rect(screen, "black", pygame.Rect(1520,100, 10, screenY - 200 ))
    
    

    



def playerDraw(screen, posX, posY, sizeX, sizeY, outside, attack, health, mana, screenX, screenY, paused):
    shield = ""
    if outside and attack and not paused: 
        shield = pygame.draw.rect(screen, (161, 5, 33), pygame.Rect(posX -50, posY -  50, 125, 125 ))
        borderN = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX -50, posY -  50, 125, 5 ))
        borderS = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX -50, posY +  70, 125, 5 ))
        borderW = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX - 50, posY - 50, 5, 125 ))
        borderE = pygame.draw.rect(screen, (112, 0, 20), pygame.Rect(posX + 70, posY - 50, 5, 125 ))
        mana -= 0.1
    else:
        if mana < 50 and not paused:
            mana += 0.01
    
    player = pygame.draw.rect(screen, "white", pygame.Rect(posX, posY, sizeX, sizeY))
    playerColor = pygame.draw.rect(screen, (47, 60, 77), pygame.Rect(posX+ 5, posY+ 5, sizeX-10, sizeY-10))

    healthEmpty = pygame.draw.rect(screen, "white", pygame.Rect(screenX//2 - 255, screenY - 85, 510, 30))
    healthMeter = pygame.draw.rect(screen, "red", pygame.Rect(screenX//2 - 250, screenY - 80, health*5, 20))

    manaEmpty = pygame.draw.rect(screen, "white", pygame.Rect(screenX//2 - 255, screenY - 45, 510, 30))
    manaMeter = pygame.draw.rect(screen, "blue", pygame.Rect(screenX//2 - 250, screenY - 40, mana*5, 20))
    return player, mana, shield

def enemy(screen, posX, posY, outside, e1posX, e1posY, e1Health, paused, invItems, player, enemy1):
    if enemy1 != "deleted":
        enemy1 = ""
        if e1Health > 0:
            enHealthEmpty = pygame.draw.rect(screen, "white", pygame.Rect(e1posX - 25, e1posY - 20, 80, 10))
            enHealthMeter = pygame.draw.rect(screen, "red", pygame.Rect(e1posX -23, e1posY - 18, e1Health*2.5333, 6))
            enemy1 = pygame.draw.rect(screen, "red", pygame.Rect(e1posX, e1posY, 30, 30))
            if not paused:
                if posX > e1posX:
                    e1posX += 2
                else:
                    e1posX -= 2

                if posY > e1posY:
                    e1posY += 2
                else:
                    e1posY -= 2
        else:
            invItems, enemy1 = drops(screen, "blocky_blood", e1posX, e1posY, invItems, player, enemy1)
    return enemy1, e1posX, e1posY, e1Health, invItems




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
    list2X = []
    list2Y = []
    for i in map:
        #telY += 120
        telX = 0
        string = i.split()
        for x in string:
            #telX += 120
            if int(x) == 1:
                listX.append(telX)
                listY.append(telY)
            if int(x) == 2:
                print("HEY")
                list2X.append(telX)
                list2Y.append(telY)
            telX += 60
        telY += 60
    mapCalcd = True
    return listX, listY, list2X, list2Y, mapCalcd
        
def outsideDrawMap(screen, listX, listY, list2X, list2Y):
    tel = 0
    while tel <= len(listX):
        try:
            mapBuild = pygame.draw.rect(screen, (0, 101, 168), pygame.Rect(listX[tel], listY[tel], 60, 60))
        except:
            pass # er komt error 1k in de zoveel frames idk waarom(uhm niet meer denk ik idk wa ik bedoelde)
        tel += 1

    tel2 = 0
    while tel2 <= len(list2X):
        try:
            mapBuild = pygame.draw.rect(screen, (1, 46, 13), pygame.Rect(list2X[tel2], list2Y[tel2], 60, 60))
        except:
            pass
        tel2 += 1

def outsideDraw(screen, screenX, screenY):
    width = 0
    house = pygame.draw.rect(screen, "red", pygame.Rect(200, 100, 300, 200))
    houseEntrance = pygame.draw.rect(screen, "black", pygame.Rect(310, 290, 80, 20))

    armory = pygame.draw.rect(screen, (46, 46, 46), pygame.Rect(400, screenY - 250, 120, 220))
    armoryEntrance = pygame.draw.rect(screen, "black", pygame.Rect(515, screenY - 90, 15, 40))

    wildEntrance = pygame.draw.rect(screen, "black", pygame.Rect(screenX - 20, screenY/2, 20, 200))

    return houseEntrance, armoryEntrance, wildEntrance

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


def collissions(screen, outside, house, armory, door, player, sizeX, sizeY, houseEntrance, armoryEntrance, wildEntrance, dt, speed, posX, posY, shop, use, screenX, screenY, shopSel, enemy1, health, e1Health, shield, paused, wild, mapCalcd):
    if outside:
        if shield and enemy1 and not paused and enemy1 != "deleted":
            if shield.colliderect(enemy1):
                e1Health -= 1
        if enemy1 and not paused and enemy1 != "deleted":
            if player.colliderect(enemy1): 
                health -= 1



        if player.colliderect(wildEntrance):
            if wild:
                house = False
                armory = False
                outside = True
                wild = False
                posX = 100
                posY = screenY/2
                mapCalcd = False
            elif not wild:
                house = False
                armory = False
                outside = True
                wild = True
                posX = 100
                posY = screenY/2
                mapCalcd = False
        if player.colliderect(houseEntrance):
            house = True
            armory = False
            outside = False
            wild = False
            speed = 400*dt
            sizeX = 75
            sizeY = 75
            posX = 1520
            posY = 840
        elif player.colliderect(armoryEntrance):
            house = False
            armory = True
            outside = False
            wild = False
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
            wild = False
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
    return outside, house, armory, sizeX, sizeY, speed, posX, posY, use, health, e1Health, wild, mapCalcd


exec(open("main.py").read())#### WEGHALEN IS VOOR TESTEN ZODAT F5 KAN DOEN IN DIT BESTAND
    
