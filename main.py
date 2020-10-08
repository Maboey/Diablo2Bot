import Diablo2Functions as D2F
import FakeInput as FI
import time
import os

attackDuration = 10 # duration of an attack since enemy is spotted

#launching the game
D2F.LaunchGame()
run = True

#get remaining life percentage
lifePercentage = D2F.GetRemainingLifePercentage()
D2F.GetToTheBattleField("up_left")

while run:
    # get old and new life points values 
    oldLifePercentage = lifePercentage
    lifePercentage = D2F.GetRemainingLifePercentage()

    # detect attack and respond for 10 sec
    if lifePercentage < oldLifePercentage:
        startingTimeAttack = time.time()
        while time.time() < (startingTimeAttack + attackDuration):
            D2F.LookForAndAttackRedEnemy()
            if lifePercentage < 50:
                D2F.DrinkPotion(D2F.checkRemainingPotions())
            if not D2F.IsGameRunning:
                run = False
                break
    else:
        D2F.MoveCharacter() 

    # stop bot if game window closes
    if not D2F.IsGameRunning():
        run = False  
    
print("Bot Stopped")
os.remove("ScreenWiew.png")