#variable
boodschappen_lijst = {}
dup = False

print("Start Programma")

while True:
    
    voeg_boodschap_toe = input("Voeg een item toe ").lower()
    
    if voeg_boodschap_toe != (""):
        
        hoeveelheid=int(input("Hoeveel wilt u toevoegen "))    
         
         
        if voeg_boodschap_toe not in boodschappen_lijst:
            boodschappen_lijst.update({voeg_boodschap_toe : hoeveelheid})
        else:
            for key in boodschappen_lijst:
                # print(f"Debug: {x['boodschap']}")
                if key.lower() == voeg_boodschap_toe.lower():
                    print(f"{key.lower()} is al toegevoegd en heeft hoveelheid: {boodschappen_lijst[key]} ")
                    uitkomst = (boodschappen_lijst[key] + hoeveelheid)
                    boodschappen_lijst.update({key:uitkomst})
                    # dup = True
    # if dup != True:          
    nog_een_item_toevoegen = input('Wilt u nog een item toevoegen? ')
        # dup = False
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

#
#
#
#
#
#
#
#
#
#
#
#
