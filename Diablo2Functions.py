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
    FI.ClickXY(screenSize[0]//2,screenSize[1]//2,0)
    time.sleep(1)
    FI.ClickXY(screenSize[0]//8*7,screenSize[1]//12*11,0)
    time.sleep(3)

def GetRemainingLifePercentage():
    remainingLifePercentage = 10
    mainPlayerLifePositionX = 70
    mainPlayerLifePositionY = 510
    lifeRangeY = 550 - 510
    screenView = Image.open(FI.GetScreenImage())
    pixels = screenView.load()
    for i in range(lifeRangeY):
        pixelColor = pixels[mainPlayerLifePositionX,mainPlayerLifePositionY + i]
        if pixelColor[1]<10 and pixelColor[2]<10:
            if pixelColor[0] > 35:
                remainingLifePercentage = lifeRangeY - i
                break
        elif pixelColor[1]<20 and pixelColor[2]<20:
            if pixelColor[0] > 60:
                remainingLifePercentage = lifeRangeY - i
                break

    remainingLifePercentage = round(remainingLifePercentage/lifeRangeY*100)
    return remainingLifePercentage

def GetRemainingManaPercentage():
    remainingManaPercentage = 10
    mainPlayerManaPositionX = 730
    mainPlayerManaPositionY = 510
    ManaRangeY = 550 - 510
    screenView = Image.open(FI.GetScreenImage())
    pixels = screenView.load()
    for i in range(ManaRangeY):
        pixelColor = pixels[mainPlayerManaPositionX,mainPlayerManaPositionY + i]
        if pixelColor[0]<10 and pixelColor[1]<10:
            if pixelColor[2] > 35:
                remainingManaPercentage = ManaRangeY - i
                break
        elif pixelColor[0]<20 and pixelColor[1]<20:
            if pixelColor[2] > 60:
                remainingManaPercentage = ManaRangeY - i
                break

    remainingManaPercentage = round(remainingManaPercentage/ManaRangeY*100)
    return remainingManaPercentage

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
        FI.ClickXY(screenSize[0]//2,screenSize[1]//10,0)
        time.sleep(timeBetweenMoves)
    if direction == "down":
        FI.ClickXY(screenSize[0]//2,screenSize[1]//10*9,0)
        time.sleep(timeBetweenMoves)
    if direction == "left":
        FI.ClickXY(screenSize[0]//10,screenSize[1]//2,0)
        time.sleep(timeBetweenMoves)
    if direction == "right":
        FI.ClickXY(screenSize[0]//10*9,screenSize[1]//2,0)
        time.sleep(timeBetweenMoves)

def RandomAttackClose():
    screenSize = FI.GetScreenSize()
    screenCenter = [screenSize[0]//2,screenSize[1]//2]
    attackRange = screenSize[1]//10
    FI.ClickXY(screenCenter[0]-attackRange,screenCenter[1]-attackRange,0)
    time.sleep(0.25)
    FI.ClickXY(screenCenter[0]+attackRange,screenCenter[1]-attackRange,0)
    time.sleep(0.25)
    FI.ClickXY(screenCenter[0]-attackRange,screenCenter[1]+attackRange,0)
    time.sleep(0.25)
    FI.ClickXY(screenCenter[0]+attackRange,screenCenter[1]+attackRange,0)
    time.sleep(0.25)

def DrinkPotion():
    for i in range(4):
            if not(IsGameRunning()):
                break
            FI.KeyboardInput(str(i+1))
            lifePercentage = GetRemainingLifePercentage()
            if lifePercentage > 25:
                break
    
def GetToTheBattleField(track):
    if track == "down_left":
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
        MoveCharacter(False,"left")
        MoveCharacter(False,"down")
        MoveCharacter(False,"left")
    if track == "down_right":
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"right")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"right")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"right")
        MoveCharacter(False,"down")
        MoveCharacter(False,"down")

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
        FI.ClickXY(enemyPosition[0],enemyPosition[1],0)
        time.sleep(0.5)
    return enemyFound