import random
aantal_keer_vragen = 3
lootjes = []
namen = []
gekozen_lootjes = []
# all_presents = {}
presents = {}
giver_reciever = {}
print('start programma')


while True:
    print(f"u moet nog minimaal {aantal_keer_vragen} mensen invullen ")
    
    if aantal_keer_vragen == 3:
        print('Vul een naam in: ')
        invullen_namen = input('>> ')
        presents[invullen_namen] = []
        count = 0
        while count < 3:
            cadeautje = input("vul een cadeautje in: ")
            presents[invullen_namen].append(cadeautje)
            count += 1
        print('')
    else:
        print('vul nog een naam in: ')
        invullen_namen = input('>> ')
        print('')
        count1 = 0
        while count1 < 3:
            cadeautje = input("vul een cadeautje in: ")
            presents.setdefault(invullen_namen, []).append(cadeautje)
            count1 += 1

    aantal_keer_vragen -= 1
    if invullen_namen not in namen:
        namen.append(invullen_namen)
        lootjes.append(invullen_namen)
        
    else:
        print("deze naam heb je al ingevuld")
        aantal_keer_vragen +=1
        
    if aantal_keer_vragen <= 0:
        print("wilt u nog een persoon toevoegen? ")
        nog_een_persoon_invullen = input('>> ')
        print('')
        if nog_een_persoon_invullen == "nee":
            break

print('')     
# random.shuffle(namen)
# random.shuffle(lootjes)
laatst_gekozen = ""
laatste_lootje = ""
while True:
    for naam in namen: # loop door je lijst me ingevulde namen heen 
        random_lootje = random.choice(lootjes)
        giver_reciever.update({naam : random_lootje})
        # print(giver_reciever)
        lootjes.remove(random_lootje)
    #check poging
    for x , y in giver_reciever.items():
        if x == y:
            lootjes = namen.copy()
            break    
    if x != y:
        break

while True:
                
    print ('Welke naam wil je opvragen:')
    
    print("")
    
    for naam in giver_reciever:
        print(naam)
    print("")
    naam_opvragen = input(">> ") 
    for key in giver_reciever.keys(): 
        if naam_opvragen == key:
            naam_1 = giver_reciever[key]
            naam = presents[naam_1]
            
            print(f'je heb het lootje van {key} gekozen')
            print(f'cadeautijes van {naam}: {naam}')
            print(f'{key.capitalize()} heeft het lootje van {naam_1.capitalize()}' )
            
    print("")
    
    print('druk op "ENTER" om nog een naam in te vullen of druk op "X" om te cancelen')
    verder_gaan =input(">> ")
    if verder_gaan == "":       
        print("")
    
    else:
        verder_gaan == "x"
        exit()