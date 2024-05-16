from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

#wit
robotArm.moveRight()
for x in range (3):
    
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

    #rood
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft() v  
robotArm.wait()