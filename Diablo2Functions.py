"""
Diablo2 Functions
"""

import time
import os
import FakeInput as FI
from PIL import Image
import random

def LaunchGame():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../DiabloII.exe')
    os.system(filename)
    time.sleep(5)
    FI.KeyboardInput('enter')
    time.sleep(1)
    FI.KeyboardInput('enter')
    time.sleep(1)
    FI.KeyboardInput('enter')
    screenSize = FI.GetScreenSize()
    print("ScreenSize : X = ", str(screenSize[0]),", Y = ", str(screenSize[1]))
    FI.ClickXY(screenSize[0]//2,screenSize[1]//2)
    time.sleep(1)
    FI.ClickXY(screenSize[0]//8*7,screenSize[1]//12*11)
    time.sleep(3)

def GetRemainingLifePercentage():
    lifePercentage = 0
    lifePosX = 69
    lifeMinPosY = 577
    lifeMaxPosY = 508
    
    screenView = Image.open(FI.GetScreenImage())
    pixels = screenView.load()
    for yRange in range (lifeMinPosY-lifeMaxPosY):
        color = pixels[lifePosX,lifeMaxPosY+yRange]
        if color[0] > (2*color[1]) and color[0]> (2*color[2]):
            lifePercentage = round((((lifeMinPosY-lifeMaxPosY)-yRange)/(lifeMinPosY-lifeMaxPosY))*100)
            break
    return lifePercentage

def GetRemainingManaPercentage():
    manaPercentage = 0
    manaPosX = 726
    manaMinPosY = 577
    manaMaxPosY = 508

    screenView = Image.open(FI.GetScreenImage())
    pixels = screenView.load()
    for yRange in range (manaMinPosY-manaMaxPosY):
        color = pixels[manaPosX,manaMaxPosY+yRange]
        if color[2] > (2*color[1]) and color[2]> (2*color[0]):
            manaPercentage = round((((manaMinPosY-manaMaxPosY)-yRange)/(manaMinPosY-manaMaxPosY))*100)
            break
    return manaPercentage

def MoveCharacter(randomChoice = True,direction = ""):
    timeBetweenMoves = 0.6
    if randomChoice:
        choice = random.randrange(0,100)
        if choice <= 25:
            direction = "up"
        elif choice <= 50:
            direction = "down"
        elif choice <= 75:
            direction = "right"
        elif choice <= 100:
            direction = "left"
    screenSize = FI.GetScreenSize()
    if direction == "up":
        FI.ClickXY(screenSize[0]//2,screenSize[1]//10)
        time.sleep(timeBetweenMoves)
    if direction == "down":
        FI.ClickXY(screenSize[0]//2,screenSize[1]//10*9)
        time.sleep(timeBetweenMoves)
    if direction == "left":
        FI.ClickXY(screenSize[0]//10,screenSize[1]//2)
        time.sleep(timeBetweenMoves)
    if direction == "right":
        FI.ClickXY(screenSize[0]//10*9,screenSize[1]//2)
        time.sleep(timeBetweenMoves)

def RandomAttackClose():
    screenSize = FI.GetScreenSize()
    screenCenter = [screenSize[0]//2,screenSize[1]//2]
    attackRange = screenSize[1]//10
    FI.ClickXY(screenCenter[0]-attackRange,screenCenter[1]-attackRange)
    time.sleep(0.25)
    FI.ClickXY(screenCenter[0]+attackRange,screenCenter[1]-attackRange)
    time.sleep(0.25)
    FI.ClickXY(screenCenter[0]-attackRange,screenCenter[1]+attackRange)
    time.sleep(0.25)
    FI.ClickXY(screenCenter[0]+attackRange,screenCenter[1]+attackRange)
    time.sleep(0.25)

def checkRemainingPotions():
    screenView = Image.open(FI.GetScreenImage())
    pixels = screenView.load()
    remainingPotions = ["None","None","None","None"]
    lifePotionsColor = [173,41,24]
    manaPotionsColor = [49,49,156]
    potion1Location = [436,578]
    potion2Location = [467,578]
    potion3Location = [498,578]
    potion4Location = [529,578]
    potionsLocations = [potion1Location,potion2Location,potion3Location,potion4Location]
    for potionsLocation in potionsLocations:
        if pixels[potionsLocation[0],potionsLocation[1]] == lifePotionsColor:
            remainingPotions[potionsLocation.index] = "lifePotion"
        elif pixels[potionsLocation[0],potionsLocation[1]] == manaPotionsColor:
            remainingPotions[potionsLocation.index] = "manaPotion"
    return remainingPotions

def DrinkPotion(remainingPotions):
    for potion in remainingPotions:
        if potion == "lifePotion":
            FI.KeyboardInput(str(potion.index))
            break  
    
def GetToTheBattleField(track):

    if track == "down_left":
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")

    if track == "down_right":
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")

    if track == "up_left":
        MoveCharacter(False,"left")
        MoveCharacter(False,"left")
        MoveCharacter(False,"up")
        MoveCharacter(False,"left")
        MoveCharacter(False,"up")
        MoveCharacter(False,"left")
        MoveCharacter(False,"up")
        MoveCharacter(False,"left")
        MoveCharacter(False,"up")
        MoveCharacter(False,"left")
        MoveCharacter(False,"left")
        MoveCharacter(False,"up")
        MoveCharacter(False,"up")

    if track == "up_right":
        MoveCharacter(False,"right")
        MoveCharacter(False,"up")
        MoveCharacter(False,"right")
        MoveCharacter(False,"up")
        MoveCharacter(False,"right")
        MoveCharacter(False,"up")
        MoveCharacter(False,"right")
        MoveCharacter(False,"up")
        MoveCharacter(False,"right")
        MoveCharacter(False,"right")
        MoveCharacter(False,"up")
        MoveCharacter(False,"up")   

def IsGameRunning():
    screenView = Image.open(FI.GetScreenImage())
    pixels = screenView.load()
    pixelColor = pixels[6,567]
    if pixelColor[0] == 74 and pixelColor[1] == 74 and pixelColor[2] == 74:
        return True
    else:
        return False

def LookForAndAttackRedEnemy():
    enemyFound = False
    enemyPosition = [0,0]
    screenView = Image.open(FI.GetScreenImage())
    screenSize = FI.GetScreenSize()
    rangeHitAroundPlayer = 100
    pixels = screenView.load()

    rangeHitAroundPlayerStartingX = (screenSize[0]//2) - rangeHitAroundPlayer
    rangeHitAroundPlayerStartingY = (screenSize[1]//2) - rangeHitAroundPlayer

    for x in range(rangeHitAroundPlayer*2):
        for y in range(rangeHitAroundPlayer*2):
            pixel0 = pixels[rangeHitAroundPlayerStartingX + 0 + x,rangeHitAroundPlayerStartingY + y + 0]
            pixel1 = pixels[rangeHitAroundPlayerStartingX + 1 + x,rangeHitAroundPlayerStartingY + y + 0]
            pixel2 = pixels[rangeHitAroundPlayerStartingX + 2 + x,rangeHitAroundPlayerStartingY + y + 0]
            pixel3 = pixels[rangeHitAroundPlayerStartingX + 0 + x,rangeHitAroundPlayerStartingY + y + 1]
            pixel4 = pixels[rangeHitAroundPlayerStartingX + 1 + x,rangeHitAroundPlayerStartingY + y + 1]
            pixel5 = pixels[rangeHitAroundPlayerStartingX + 2 + x,rangeHitAroundPlayerStartingY + y + 1]
            pixel6 = pixels[rangeHitAroundPlayerStartingX + 0 + x,rangeHitAroundPlayerStartingY + y + 2]
            pixel7 = pixels[rangeHitAroundPlayerStartingX + 1 + x,rangeHitAroundPlayerStartingY + y + 2]
            pixel8 = pixels[rangeHitAroundPlayerStartingX + 2 + x,rangeHitAroundPlayerStartingY + y + 2]
            pixelArrow = [pixel0,pixel1,pixel2,pixel3,pixel4,pixel5,pixel6,pixel7,pixel8]
            for p in pixelArrow:
                if  p[0] > 100 and p[1] < 40 and p[2] < 40:
                    enemyPosition = [rangeHitAroundPlayerStartingX + x + 2,rangeHitAroundPlayerStartingY + y + 2]
                    enemyFound = True
                    break
    if enemyFound:
        FI.ClickXY(enemyPosition[0],enemyPosition[1])
        time.sleep(0.5)
    return enemyFound


