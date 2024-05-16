from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
aantal_stappen = 0
aantal_blokken = 0
# Jouw python instructies zet je vanaf hier:
for x in range(7):
    robotArm.grab()
    #print(robotArm.scan()) for debugging
    if robotArm.scan() != '':
        aantal_blokken +=1
    else:
        break  
    for x in range (aantal_blokken):
        robotArm.moveRight()
    robotArm.drop()
    for x in range (aantal_blokken):
        robotArm.moveLeft()
        
  

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

