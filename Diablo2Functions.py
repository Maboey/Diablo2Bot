"""
Diablo2 Functions
"""

import time
import os
import FakeInput as FI
from PIL import Image
import random
import keyboard

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
    pixels = FI.GetScreenPixels()
    for yRange in range (lifeMinPosY-lifeMaxPosY):
        color = pixels[lifePosX,lifeMaxPosY+yRange]
        if color[0] > (2*color[1]) and color[0]> (2*color[2]):
            lifePercentage = round((((lifeMinPosY-lifeMaxPosY)-yRange)/(lifeMinPosY-lifeMaxPosY))*100)
            print("Remaining Life = " + str(lifePercentage) + "%")
            break
    return lifePercentage

def GetRemainingManaPercentage():
    manaPercentage = 0
    manaPosX = 726
    manaMinPosY = 577
    manaMaxPosY = 508
    pixels = FI.GetScreenPixels()
    for yRange in range (manaMinPosY-manaMaxPosY):
        color = pixels[manaPosX,manaMaxPosY+yRange]
        if color[2] > (2*color[1]) and color[2]> (2*color[0]):
            manaPercentage = round((((manaMinPosY-manaMaxPosY)-yRange)/(manaMinPosY-manaMaxPosY))*100)
            print("Remaining Mana = " + str(manaPercentage) + "%")
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
    print("moved " + direction)

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
    print("attacked at random")

def checkRemainingPotions():
    pixels = FI.GetScreenPixels()
    remainingPotions = ["None","None","None","None"]
    potion1Location = [436,578]
    potion2Location = [467,578]
    potion3Location = [498,578]
    potion4Location = [529,578]
    potionsLocations = [potion1Location,potion2Location,potion3Location,potion4Location]
    arrayIndex = 0
    for potionsLocation in potionsLocations:
        pixelColor = pixels[potionsLocation[0],potionsLocation[1]]
        if  pixelColor[0] > (2*pixelColor[1]) and pixelColor[0] > (2*pixelColor[2]):
            remainingPotions[arrayIndex] = "lifePotion"
        elif pixelColor[2] > (2*pixelColor[1]) and pixelColor[2] > (2*pixelColor[0]):
            remainingPotions[arrayIndex] = "manaPotion"
        arrayIndex += 1
    print("remaining potions = " + remainingPotions[0] + ","+ remainingPotions[1] + ","+ remainingPotions[2] + ","+ remainingPotions[3])
    return remainingPotions

def DrinkPotion(remainingPotions):
    potionIndex = 1
    for potion in remainingPotions:
        if potion == "lifePotion":
            FI.KeyboardInput(str(potionIndex))
            print("Drinks 1 Life Potion")
            break  
        potionIndex += 1
    
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
    pixels = FI.GetScreenPixels()
    pixelColor = pixels[6,567]
    if pixelColor[0] == 74 and pixelColor[1] == 74 and pixelColor[2] == 74:
        return True
    else:
        return False

def LookForAndAttackRedEnemy():
    enemyFound = False
    enemyPosition = [0,0]
    screenSize = FI.GetScreenSize()
    rangeHitAroundPlayer = 100
    pixels = FI.GetScreenPixels()
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
        # hold shift to prevent character movement and release after attack
        keyboard.press("shift")
        FI.ClickXY(enemyPosition[0],enemyPosition[1])
        keyboard.release("shift")
        time.sleep(0.2)
    return enemyFound

def LookForAndGrabItems():
    keyboard.press("alt")
    itemFound = False
    itemPosition = [0,0]
    screenSize = FI.GetScreenSize()
    rangeHitAroundPlayer = 200
    pixels = FI.GetScreenPixels()
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
                if  p[0] > 200 and p[1] > 200 and p[2] > 200:
                    itemPosition = [rangeHitAroundPlayerStartingX + x + 2,rangeHitAroundPlayerStartingY + y + 2]
                    itemFound = True
                    break
    if itemFound:
        FI.ClickXY(itemPosition[0],itemPosition[1])
        keyboard.release("alt")
        time.sleep(0.2)
    return itemFound
