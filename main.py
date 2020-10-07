import Diablo2Functions as D2F
import FakeInput as FI
import time
import os

D2F.LaunchGame()
run = True
lifePercentage = D2F.GetRemainingLifePercentage()
D2F.GetToTheBattleField("down_left")
while run:
# get old and new life points values 
    oldLifePercentage = lifePercentage
    lifePercentage = D2F.GetRemainingLifePercentage()

# stop bot if game window closes
    if not D2F.IsGameRunning():
        run = False
    
# caracter attitude
    if lifePercentage<oldLifePercentage:
        if not D2F.LookForAndAttackRedEnemy():
            if lifePercentage<25:
                D2F.DrinkPotion()
    else:
        D2F.MoveCharacter()
print("Bot Stopped")
os.remove("ScreenWiew.png")