import random
aantal_keer_vragen = 3
lootjes = []
namen = []
gekozen_lootjes = []
print('start programma')

while True:
    print(f"u moet nog minimaal {aantal_keer_vragen} mensen invullen ")
    
    if aantal_keer_vragen == 3:
        print('Vul een naam in" ')
        invullen_namen = input('>> ')
        
        print('')
    else:
        print('vul nog een naam in: ')
        invullen_namen = input('>> ')
        print('')
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
for naam in namen:
    while True:
        random_lootje = random.choice(lootjes)
        if naam != laatste_lootje:
            if naam != random_lootje:
                gekozen_lootjes.append(f'{naam} heeft het lootje van {random_lootje}')
                lootjes.remove(random_lootje)
                laatste_lootje = random_lootje
                laatst_gekozen = naam
                break
        else:
            if random_lootje != laatst_gekozen:
                    gekozen_lootjes.append(f'{naam} heeft het lootje van {random_lootje}')
                    lootjes.remove(random_lootje)
                    laatste_lootje = random_lootje
                    laatst_gekozen = naam
                    break
                            
print('--------Getrokken lootjes--------')
print("")
for x in gekozen_lootjes:
    
    print(x.capitalize())
    print("")
gekozen_lootjes = []
print('')
print('---------------------------------')



# for naam in namen:
#     while True:
#         random_lootje = random.choice(lootjes)
#         if laatst_gekozen != random_lootje:
#             if naam != random_lootje:
#                 gekozen_lootjes.append(f'{naam} heeft het lootje van {random_lootje}')
#                 lootjes.remove(random_lootje)
#                 laatste_lootje = random_lootje
#                 laatst_gekozen = naam
#                 break
            # else:
            #     break












# print(f'{naam} heeft het lootje van {lootje}')
# random value uit de 2 lijstjes
# lootjes = random.choice(namen)
# random_nummers = random.choice(nummer)
# print(lootjes , random_nummers)
