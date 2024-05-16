from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
herhalingen = 0
aantal_stappen = 0
# Jouw python instructies zet je vanaf hier:


robotArm.grab()
while aantal_stappen <9:
    robotArm.moveRight()   
    aantal_stappen +=1
robotArm.drop()
aantal_stappen = 0

#tweede blok
while aantal_stappen < 6:
    robotArm.moveLeft()
    aantal_stappen +=1
robotArm.grab()    
aantal_stappen = 0
while aantal_stappen < 6:
    robotArm.moveRight()
    aantal_stappen += 1 
robotArm.drop()
aantal_stappen = 0

#3e blok
while aantal_stappen < 3:
    robotArm.moveLeft()
    aantal_stappen +=1
robotArm.grab()
aantal_stappen = 0

while aantal_stappen <3:
    robotArm.moveRight()
    aantal_stappen +=1
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()