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
D2F.GetToTheBattleField("down_left")

while run:
    # get old and new life points values 
    oldLifePercentage = lifePercentage
    lifePercentage = D2F.GetRemainingLifePercentage()
    print("RemainingLife = " + str(lifePercentage) + "%")

    # detect attack and respond for 10 sec
    if lifePercentage < oldLifePercentage:
        print("lost life")
        startingTimeAttack = time.time()
        print("Started Attacking")
        while time.time() < (startingTimeAttack + attackDuration):
            D2F.LookForAndAttackRedEnemy()
            if not D2F.IsGameRunning:
                run = False
                break
    else:
        D2F.MoveCharacter()
    if lifePercentage < 50:
        print("Drank 1 Life Potion")
        D2F.DrinkPotion(D2F.checkRemainingPotions())

    # stop bot if game window closes
    if not D2F.IsGameRunning():
        print("Bot Stopped")
        run = False  

os.remove("ScreenWiew.png")