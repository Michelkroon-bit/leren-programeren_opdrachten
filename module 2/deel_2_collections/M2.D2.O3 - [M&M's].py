from random import choice

kleuren = ("oranje","blauw","groen","bruin")
hoeveel_snoepjes = int(input("hoeveel m&m's moeten er toegevoegd worden: ")) 

hoeveelheid_mnms= [] 
for x in range(hoeveel_snoepjes):
    hoeveelheid_mnms.append(choice(kleuren))
print ("dit zit er in het zakje")
print(f"{hoeveelheid_mnms}")



#telt de hoeveelheid kleuren (extra)
oranje = 0
blauw = 0
groen = 0
bruin = 0
for x in hoeveelheid_mnms:
    if x == "oranje":
        oranje +=1
    elif x == "blauw":
        blauw += 1 
    elif x == "groen":
        groen += 1
    elif x == "bruin":
        bruin += 1

print("dit is de kleurverdeling")
print("")
print (f"{oranje} oranje m&m's")
print (f"{blauw} blauwe m&m's")
print (f"{groen} groene m&m's")
print (f"{bruin} bruine m&m's")