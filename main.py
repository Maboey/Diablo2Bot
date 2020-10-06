import Diablo2Functions as D2F
import FakeInput as FI
import time
import os

D2F.LaunchGame()
run = True
lifePercentage = D2F.GetRemainingLifePercentage()
D2F.GetToTheBattleField("down_right")
while run:
# get old and new life points values 
    oldLifePercentage = lifePercentage
    lifePercentage = D2F.GetRemainingLifePercentage()

# stop bot if game window closes
    if not D2F.IsGameRunning():
        run = False
    
# character attitude
    #if life is low drink potion else try to find enemy and if there's no one just walk randomly
    if lifePercentage < 50:
        D2F.DrinkPotion()
    elif not D2F.LookForAndAttackRedEnemy(): # always true error in function !!!! <--------------- ERROR
        D2F.MoveCharacter()
print("Bot Stopped")
os.remove("ScreenWiew.png")


