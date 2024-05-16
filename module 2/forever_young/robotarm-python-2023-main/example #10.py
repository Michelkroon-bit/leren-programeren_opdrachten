from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
steps = 9# variable over de hoeveelheid stappen naar de overkant van het scherm
move_left = 0#variable
move_right = 0#
while steps > 0:#
    robotArm.grab()
    while move_right < steps:
        robotArm.moveRight()
        move_right +=1
    robotArm.drop()
    steps -=1 
    while move_left < steps:
        robotArm.moveLeft()
        move_left+=1
    steps -=1
    move_left=0#reset voor while loops
    move_right=0#reset voor while loops
        
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#