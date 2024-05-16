from fruitmand import *
import random
aantal = int(input("Vul een aantal in: "))

for x in range(aantal):
    print(fruitmand[random.randint(0,6)]['name']) 
    
    