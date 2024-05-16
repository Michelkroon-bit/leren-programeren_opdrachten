#variable
boodschappen_lijst = {}
dup = False

print("Start Programma")

while True:
    
    voeg_boodschap_toe = input("Voeg een item toe ")
    
    if voeg_boodschap_toe != (""):
        
        hoeveelheid=int(input("Hoeveel wilt u toevoegen "))    
         
         
        if voeg_boodschap_toe not in boodschappen_lijst:
            boodschappen_lijst.update({voeg_boodschap_toe : hoeveelheid})
        else:
            for key in boodschappen_lijst:
                if key.lower() == voeg_boodschap_toe.lower():
                    print(f"{key.lower()} is al toegevoegd en heeft hoveelheid: {boodschappen_lijst[key]} ")
                    uitkomst = (boodschappen_lijst[key] + hoeveelheid)
                    boodschappen_lijst.update({key:uitkomst})      
    nog_een_item_toevoegen = input('Wilt u nog een item toevoegen? ')
    if nog_een_item_toevoegen == "nee":

        break
print("")
print('-[Boodschappenlijst]-')
print("")
for key in boodschappen_lijst:
    print(f" {key} x {boodschappen_lijst[key]}")
print("")
print('---------------------')
        
#verbetering

#1 dictionairy gebruiken
#code vereenvoudigen
#per item dat je wilt kopen 1 element 
#als het item al in de dict staat dan voegt hij alleen de hoeveelheid toe
#als het item er niet in staat wordt hij gewoon toegevoegd
#
#
#
#
#
#
#
#