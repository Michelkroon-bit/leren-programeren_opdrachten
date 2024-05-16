# def score(dice):
#     points = 0
#     een_gerold = 0
#     twee_gerold = 0
#     drie_gerold = 0
#     vier_gerold = 0
#     vijf_gerold = 0
#     zes_gerold = 0
    
#     for x in dice:
#         if x == 1:
#             een_gerold += 1
#             if een_gerold == 3:
#                 points += 1000
#                 een_gerold = 0 
#             else:
#                 points += 100

#         elif x == 2:
#             twee_gerold += 1
#             if twee_gerold == 3:
#                 points += 200
#                 twee_gerold = 0

#         elif x == 3:
#             drie_gerold += 1
#             if drie_gerold == 3:
#                 points += 300
#                 drie_gerold = 0

#         elif x == 4:
#             vier_gerold += 1
#             if vier_gerold >= 3:
#                 points += 400

#         elif x == 5:
#             vijf_gerold += 1
#             if vijf_gerold == 3:
#                 points += 500
#                 vijf_gerold = 0
#             else:
#                 points += 50

#         elif x == 6:
#             zes_gerold += 1
#             if zes_gerold >= 3:
#                 points += 600

#     print(f'punten: {points}')
#     return points




# score([5, 1, 3, 4, 1])
# score([1, 1, 1, 3, 1])
# score([2, 3, 4, 6, 2])
# score([4, 4, 4, 3, 3])
# score([2, 4, 4, 5, 4])


# Eerst maak je de nieuwe dictionary
import random

aantal_keer_vragen = 3
lootjes = []
namen = []
gekozen_lootjes = []
all_presents = {}
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
        while count < 3:
            cadeautje = input("vul een cadeautje in: ")
            presents[invullen_namen].append(cadeautje)
            count += 1

    aantal_keer_vragen -= 1
    if invullen_namen not in namen:
        namen.append(invullen_namen)
        lootjes.append(invullen_namen)
        
    else:
        print("deze naam heb je al ingevuld")
        aantal_keer_vragen += 1
        
    if aantal_keer_vragen <= 0:
        print("wilt u nog een persoon toevoegen? ")
        nog_een_persoon_invullen = input('>> ')
        print('')
        if nog_een_persoon_invullen == "nee":
            break

# Voeg alle cadeautjes toe aan all_presents
all_presents.update(presents)

print('')     
laatst_gekozen = ""
laatste_lootje = ""
while True:
    for naam in namen: 
        random_lootje = random.choice(lootjes)
        giver_reciever.update({naam: random_lootje})
        lootjes.remove(random_lootje)
    
    for x, y in giver_reciever.items():
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
            naam = presents[key]
            
            print(f'Je hebt het lootje van {key} gekozen')
            print(f'Cadeautijes van {key}: {naam}')
            print(f'{key.capitalize()} heeft het lootje van {naam_1.capitalize()}' )
            
    print("")
    
    print('Druk op "ENTER" om nog een naam in te vullen of druk op "X" om te cancelen')
    verder_gaan = input(">> ")
    if verder_gaan == "":       
        print("")
    
    else:
        verder_gaan == "x"
        exit() 
