from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)
aantal_stappen = 0
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
while robotArm.scan() !=(""):
    aantal_stappen+=1
    for x in range (aantal_stappen):
        robotArm.moveRight()
    robotArm.drop()
    for x in range (aantal_stappen):
        robotArm.moveLeft()
    robotArm.grab()   
  

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

