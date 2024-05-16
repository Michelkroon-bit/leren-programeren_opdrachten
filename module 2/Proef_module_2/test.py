import random



while True:
    aantal_keer_vragen = 3
    lootjes = ['mama', 'michel', 'papa']
    namen = ['papa', 'mama', 'michel']
    gekozen_lootjes = []

    giver_reciever = {}
    print('start programma')

        
    # random.shuffle(namen)
    # random.shuffle(lootjes)
    laatst_gekozen = ""
    laatste_lootje = ""
    for naam in namen:
        while True:
            random_lootje = random.choice(lootjes)
            giver_reciever.update({naam : random_lootje})
            if naam == random_lootje:
                giver_reciever.clear()
            else:
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
                print(f'je heb het lootje van {key} gekozen')
                print(f'{key.capitalize()} heeft het lootje van {naam_1.capitalize()}' )
                
        print("")
        
        print('druk op "ENTER" om nog een naam in te vullen of druk op "X" om te cancelen')
        verder_gaan =input(">> ")
        if verder_gaan == "":       
            print("")
        
        else:
            verder_gaan == "x"
            exit()
                    

        for x, y in giver_reciever.items():
            print(x, y)
            
        input("Press enter to run again.")
