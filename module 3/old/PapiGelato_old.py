import time
from functions import *
from data import *
from typmachine_prints import *
#maak_bestelling =""
bestellingen_lijst = []

som = 0
aantal_hoorntjes = 0
aantal_bakjes = 0

fast_typemachine_print('''         _
       ,' `,.
       >-.(__)
      (_,-' |
        `.  |
          `.|
            `\n''')


rainbow_typemachine_print('🍦Welkom bij Papi Gelato🍦\n')


while True:
    bestelde_items = get_bestelling()
    bestellingen_lijst.append(bestelde_items)
    print(bestellingen_lijst)
    print('\n')
    typemachine_print(f"Uw bestelling is toegevoegd: een {bestelde_items['bakje/hoorntje']} met {bestelde_items['ijsje']} bolletjes\n")
    print('\n')
    
    typemachine_print(f"Wilt u nog iets bestellen?\n")
    nog_iets_bestellen = input("")
    if nog_iets_bestellen in ('N','n','NEE','nee','Nee'):
        
        break


#--> check hoeveel er van ieder is <--#
for x in bestellingen_lijst:
    som += x['ijsje']
    if x['bakje/hoorntje'] == "bakje":
        aantal_bakjes += 1
    elif x['bakje/hoorntje'] == "hoorntje":
        aantal_hoorntjes +=1





#toegevoegd
prijs_toppings = 0
for t in bestellingen_lijst:
    if t['topping'] == "Slagroom":
        prijs_toppings += SLAGROOM
    elif t['topping'] == "Sprinkels":
        hoeveelheid_sprinkels  = SPRINKELS * som
        prijs_toppings += hoeveelheid_sprinkels
    if t["bakje/hoorntje"] == "bakje" and t['topping'] == "Caramel Saus":
        prijs_toppings += CARAMEL_SAUS_IN_BAKJE
    elif t["bakje/hoorntje"] == "hoorntje" and t['topping'] == "Caramel Saus":
        prijs_toppings += CARAMEL_SAUS_IN_HOORNTJE
    round(prijs_toppings)
#toegevoegd

#--> de som <--#
prijs_per_bolletje = som * PRIJS_PER_BOLLETJES 
round(prijs_per_bolletje)
prijs_per_bakje = aantal_bakjes * BAKJES
round(prijs_per_bakje)
prijs_per_hoorntje = aantal_hoorntjes * HOORNTJE
round(prijs_per_hoorntje)
totaal = prijs_per_hoorntje + prijs_per_bakje + prijs_per_bolletje + prijs_toppings
round(totaal)
#--> bonnetje <--#


print('--------["Papi Gelato"]------------')

# print(f"Bolletjes        
for x in bestellingen_lijst:
    if x['bakje/hoorntje'] == "bakje":
        print('')
        print(f"Bakje            1 x {BAKJES} =   €{round(prijs_per_bakje ,2 )}")
        

    if x['bakje/hoorntje'] == 'hoorntje':
        print('')
        print(f"Hoorntje         1 x {HOORNTJE} =   €{round(prijs_per_hoorntje ,2 )}")

    for s in x['smaak']:
        lenwhitespaces = MAX_LENGTH - len(s)
        teller = 0
        white_space = ""
        
        while teller <= lenwhitespaces:
            white_space += " "
            teller +=1
            
        print(f"  b.{s}{white_space}1 x {PRIJS_PER_BOLLETJES:.2f} =   €{PRIJS_PER_BOLLETJES:.2f}")


print("")
print(f"toppings                =     €{prijs_toppings:.2f}")
prijs_toppings = 0
print('                        --------- +')
print(f'totaal                    = €  {totaal:.2f}')
typemachine_print(f"🍦{BEDANKT_EN_TOT_ZIENS}🍦\n")


