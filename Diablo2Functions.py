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
    filename = os.path.join(dirname, '../Game/DiabloII.exe')
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
    lifeRangeY = 578 - 510
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
    ManaRangeY = 578 - 510
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
    if randomChoice:
        choice = random.randrange(1,4)
        if choice == 2:
            direction = "up"
        if choice == 1:
            direction = "down"
        if choice == 4:
            direction = "right"
        if choice == 3:
            direction = "left"
    screenSize = FI.GetScreenSize()
    if direction == "up":
        FI.ClickXY(screenSize[0]//2,screenSize[1]//10,0)
    if direction == "down":
        FI.ClickXY(screenSize[0]//2,screenSize[1]//10*9,0)
    if direction == "left":
        FI.ClickXY(screenSize[0]//10,screenSize[1]//2,0)
    if direction == "right":
        FI.ClickXY(screenSize[0]//10*9,screenSize[1]//2,0)

def RandomAttackClose():
    screenSize = FI.GetScreenSize()
    screenCenter = [screenSize[0]//2,screenSize[1]//2]
    rangeTryAttackX = screenSize[0]//6
    rangeTryAttackY = screenSize[1]//3
    startingPointX = screenCenter[0]-(rangeTryAttackX//2)
    startingPointY = screenCenter[1]-(rangeTryAttackY//2)

    for i in range(rangeTryAttackX//5):
        for j in range(rangeTryAttackY//5):
            FI.ClickXY(startingPointX+i*5,startingPointY+j*5,0)

def DrinkPotion(option):
    FI.KeyboardInput(option)
    
def GetToTheBattleField():
    MoveCharacter(False,"down")
    time.sleep(1)
    MoveCharacter(False,"left")
    time.sleep(1)
    MoveCharacter(False,"down")
    time.sleep(1)
    MoveCharacter(False,"left")
    time.sleep(1)
    MoveCharacter(False,"down")
    time.sleep(1)
    MoveCharacter(False,"left")
    time.sleep(1)
    MoveCharacter(False,"down")
    time.sleep(1)
    MoveCharacter(False,"left")
    time.sleep(1)
    MoveCharacter(False,"down")
    time.sleep(1)
    MoveCharacter(False,"left")
    time.sleep(1)

    
    