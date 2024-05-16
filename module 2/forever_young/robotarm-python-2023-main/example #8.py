from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
blokje = 0
while blokje < 7:
    robotArm.grab()
    aantal_stappen = 0
    while aantal_stappen <8:
        robotArm.moveRight()
        aantal_stappen +=1

    robotArm.drop()
    if blokje <= 5:
        stappen_terug = 0
        while stappen_terug <8:
            robotArm.moveLeft()
            stappen_terug+= 1
    blokje+= 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#