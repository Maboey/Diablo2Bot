import Diablo2Functions as D2F
import FakeInput as FI
import time

D2F.LaunchGame()
alive = True
lifePercentage = D2F.GetRemainingLifePercentage()
D2F.GetToTheBattleField()
while alive:
    oldLifePercentage = lifePercentage
    lifePercentage = D2F.GetRemainingLifePercentage()
    if lifePercentage <= 10:
        alive = False
    if lifePercentage < 25:
        for i in range(3):
            D2F.DrinkPotion(str(i+1))
            time.sleep(1)
            lifePercentage = D2F.GetRemainingLifePercentage()
            if lifePercentage > 25:
                break
    elif oldLifePercentage > lifePercentage and lifePercentage > 25:
        D2F.RandomAttackClose()
    else:1
        D2F.MoveCharacter()
    time.sleep(1)
print("you died")