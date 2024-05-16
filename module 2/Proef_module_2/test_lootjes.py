import random


aantal_keer_vragen = 3
lootjes = ['a', 'b', 'c','d','e','f']
namen = ['a', 'b', 'c','d','e','f']
gekozen_lootjes = []

giver_reciever = {}
print('start programma')

    
# random.shuffle(namen)
# random.shuffle(lootjes)

while True:
    for naam in namen: # loop door je lijst me ingevulde namen heen 
        random_lootje = random.choice(lootjes)
        giver_reciever.update({naam : random_lootje})
        # print(giver_reciever)
        lootjes.remove(random_lootje)
    print(giver_reciever)
    #check poging
    for x , y in giver_reciever.items():
        if x == y:
            lootjes = namen.copy()
            # giver_reciever.clear()
            # print(giver_reciever)
            break    
    if x != y:
        break
print(giver_reciever)