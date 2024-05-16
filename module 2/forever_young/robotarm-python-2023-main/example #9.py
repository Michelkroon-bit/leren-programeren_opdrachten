from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
afstand = 0
afstand_terug = 0 
stapel = 0
# Jouw python instructies zet je vanaf hier:

while stapel < 4:
    repeat = stapel
    afstand = 0
    afstand_terug = 0
    while repeat >= 0: 
        if repeat > 0:
            robotArm.grab()
            while afstand < 5:
                robotArm.moveRight()
                afstand+=1 
            robotArm.drop()
            while afstand_terug <5:
                robotArm.moveLeft()
                afstand_terug += 1         
        else:
            robotArm.grab()
            while afstand < 5:
                robotArm.moveRight()
                afstand+=1 
            robotArm.drop()
            if stapel <3:
                while afstand_terug <4:
                    robotArm.moveLeft()
                    afstand_terug += 1   
        afstand = 0
        afstand_terug = 0
        repeat -=1
            
    stapel +=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


