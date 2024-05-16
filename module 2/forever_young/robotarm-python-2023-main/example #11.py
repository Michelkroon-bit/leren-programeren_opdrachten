from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:

blokje = 0
herhalingen = 0
aantal_stappen = 0

while herhalingen < 2:
    robotArm.grab()
    aantal_stappen = 0
    while aantal_stappen <1:
        robotArm.moveRight()
        aantal_stappen+=1
    robotArm.drop()
    while aantal_stappen < 4:
        robotArm.moveRight()
        aantal_stappen+=1
    herhalingen+=1
while aantal_stappen <1:
    robotArm.moveRight()
    aantal_stappen +=1
robotArm.grab()
robotArm.moveRight()
robotArm.drop()    
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#