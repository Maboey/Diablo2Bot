import Diablo2Functions as D2F
import FakeInput as FI
import time
import os

attackDuration = 3 # duration of an attack since enemy is spotted

#launching the game
D2F.LaunchGame()
run = True

#get remaining life percentage
lifePercentage = D2F.GetRemainingLifePercentage()
D2F.GetToTheBattleField("down_left")

while run:
    # get old and new life points values 

    
    oldLifePercentage = lifePercentage
    lifePercentage = D2F.GetRemainingLifePercentage()

    # detect attack and respond for x sec
    if lifePercentage < oldLifePercentage:
        print("lost life")
        startingTimeAttack = time.time()
        while time.time() < (startingTimeAttack + attackDuration):
            D2F.LookForAndAttackRedEnemy()
            #if game stops, stop the attack and bot
            if not D2F.IsGameRunning:
                run = False
                break     
    else:
        #D2F.LookForAndGrabItems()
        D2F.MoveCharacter()
    if lifePercentage < 25:
        D2F.DrinkPotion(D2F.checkRemainingPotions())

    # stop bot if game window closes
    if not D2F.IsGameRunning():
        print("Bot Stopped")
        run = False  

os.remove("ScreenWiew.png")