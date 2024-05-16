from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
# blokje = 0 
# Jouw python instructies zet je vanaf hier:
afstand = 0 
while afstand < 9:  
    robotArm.moveRight()
    afstand +=1   
stapeltjes = 0
while stapeltjes < 5:
    blokje = 0
    while blokje < 6:
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        if blokje <5:
            robotArm.moveRight()
        blokje+=1  
    if stapeltjes < 4:
        robotArm.moveLeft()
    stapeltjes +=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

