import random
ronde = 1
punt = 0
print("start programma")
while ronde < 21:
    print(f"Start ronde: {ronde}")
    print("Raad een getal tussen 1 en 1000")
    random_getal = random.randint(1,1000)
    print(random_getal)
    for x in range(10):
        raden = int(input("vul hier een getal in: "))
        if raden > random_getal:
            print('lager')
        elif raden < random_getal:
            print("hoger")            
        if random_getal != raden:
            print("Fout probeer opnieuw")
            verschil = abs(random_getal-raden)
            # print(verschil)#for debugging
            if verschil > 20 and verschil <= 50:
                print("je bent warm")
            elif verschil <= 20:
                print("je bent heel warm")
            pogingen = 9 - x
            if pogingen == 0:
                print(f"helaas u heeft geen pogingen meer over het getal was {random_getal}")
            else:
                print(f"u heeft nog {pogingen} poging(en) over" ) 
        else:
            print("Goed geraden!!!")
            punt+=1
            print(f"{punt} punt(en)")
            break        
    # nog een ronde?    
    nog_een_ronde = input("Wilt u nog een ronde spelen? " )
    if ronde == 20 or nog_een_ronde == "nee":
        print(f"{punt} punten goed gedaan!!")
        print("Einde programma")
        exit()
    else:
        ronde += 1       
