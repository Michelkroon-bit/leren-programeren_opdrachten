#simple while loop

#voorbeeld 1
intstartnumber= 0# start variable (integer)
intendnumber= 6# eind variable (integer)

while intstartnumber < intendnumber: # wanneer de startnummer kleiner is dan het eind nummer wordt hij gelooped tot ze allebij gelijk zin
    print("intstartnumber : " +str(intstartnumber))# print
    intstartnumber += 1    #zorgt ervoor dat de loop niet oneindig doorgaat doormiddel van elke "loop" +1 te doen tot alle bij de variable gelijk zijn.
    
#voorbeeld 2

startnummer= 0

while startnummer < 100:
    print(startnummer)
    startnummer += 1
    


# while(conditie)   




leeftijd = 0
while leeftijd == 0:
    try:
        leeftijd = int(input('wat is je leeftijd '))
    except ValueError:
        print('je moet wel een getal invullen ')
    print('je leeftijd is' ,leeftijd )
    
    
    
    
