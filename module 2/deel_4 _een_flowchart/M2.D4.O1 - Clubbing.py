PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

vip = False
age21 = False
bandje_kleur = ""
stempel = False


#bouw hieronder de flowchart na

    #start en leeftijd 
print("start programma ")
leeftijd = int(input("Hoe oud ben je: "))
if leeftijd >= 21:
    age21=True
tijd_wachten = 18 - leeftijd
tijd_tot_21 = 21-leeftijd
if leeftijd < 18:
    print("Sorry je mag niet naar binnen")
    print(f"probeer het over {tijd_wachten} nog een keer")
else:
    
    #naam
    naam = input("wat is je naam ")
    if naam in VIP_LIST:
        vip = True
    
    #bandje blauw
    if vip and age21:
        bandje_kleur = 'blauw'
        print(f"je krijgt van mij een {bandje_kleur} bandje")

    #bandje rood
    elif vip and age21 == False:
        bandje_kleur = 'rood' 
        print(f"je krijgt van mij een {bandje_kleur} bandje")
    
    #stempel  
    elif vip == False and age21:
        print("je krijgt van mij een stempel")
        stempel = True
    else:
        print("debug: je krijg geen stempel")

    
    #drinken
    drinken  = input("wat wil je drinken? ").lower()
    if drinken in DRANKJES:
        #cola
        if drinken == "cola" and bandje_kleur != "":
            print("alstublieft, complimenten van het huis")
            print ("einde programma")
        elif drinken == "cola" and bandje_kleur == "":
            print (f"alsjeblieft je {drinken} dat is dan {PRIJS_COLA}")
            print ("einde programma")
            
        #bier
        elif drinken == "bier" and (bandje_kleur != "" or stempel == True):
            if bandje_kleur != "":
                print("alstublieft, complimenten van het huis")
                print ("einde programma")
            else:
                print (f"alsjeblieft je {drinken} dat is dan {PRIJS_BIER}")
                print ("einde programma")
        elif drinken == "bier" and (bandje_kleur == "" or stempel == False):
            print("sorry je mag nog geen alcohol bestellen onder de 21") 
            print(f"probeer het in {tijd_tot_21} jaar nog eens")
            print ("einde programma")
            
        #champagne
        elif drinken =="champagne" and bandje_kleur != "" and bandje_kleur == "blauw":
            print (f"alsjeblieft je {drinken} dat is dan {PRIJS_CHAMPAGNE}")
            print ("einde programma") 
            if drinken == "champagne" and bandje_kleur == "":
                print("sorry alleen vips mogen champagne bestellen")
                print("einde programma")
            elif drinken =="champagne" and bandje_kleur != "" and bandje_kleur != "blauw":
                print("sorry je mag geen alcohol bestellen onder de 21")
                print(f"probeer het over{tijd_tot_21} jaar nog eens")
                print("einde programma")
    else:
        print("Sorry geen idee wat je bedoeld, hier een glaasje water.")
        print("eind programma")