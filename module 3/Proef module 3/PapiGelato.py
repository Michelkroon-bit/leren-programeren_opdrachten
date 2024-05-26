import time
from function import *
from data import *
#maak_bestelling =""
bestellingen_lijst = []

som = 0
aantal_hoorntjes = 0
aantal_bakjes = 0

time.sleep(0.5)
print('''         _
       ,' `,.
       >-.(__)
      (_,-' |
        `.  |
          `.|
            `''')


typemachine_print('🍦Welkom bij Papi Gelato🍦\n')


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



#--> de som <--#
prijs_per_bolletje = som * PRIJS_PER_BOLLETJES 
round(prijs_per_bolletje)
prijs_per_bakje = aantal_bakjes * BAKJES
round(prijs_per_bakje)
prijs_per_hoorntje = aantal_hoorntjes * HOORNTJE
round(prijs_per_hoorntje)
totaal = prijs_per_hoorntje + prijs_per_bakje + prijs_per_bolletje
round(totaal)

#--> bonnetje <--#


print('--------["Papi Gelato"]------------')

# print(f"Bolletjes        
for x in bestellingen_lijst:
    if x['bakje/hoorntje'] == "bakje":
        print('')
        print(f"Bakje            {aantal_bakjes} x {BAKJES} = €  {round(prijs_per_bakje ,2 )}")
        

    if x['bakje/hoorntje'] == 'hoorntje':
        print('')
        print(f"Hoorntje         {aantal_hoorntjes} x {HOORNTJE} = €  {round(prijs_per_hoorntje ,2 )}")

    for s in x['smaak']:
        lenwhitespaces = MAX_LENGTH - len(s)
        teller = 0
        white_space = ""
        
        while teller <= lenwhitespaces:
            white_space += " "
            teller +=1
            
        print(f"  b.{s}{white_space}1 x {PRIJS_PER_BOLLETJES:.2f} = €  {prijs_per_bolletje:.2f}")

print('                          --------- +')
print(f'totaal                    = €  {totaal:.2f}')
typemachine_print(f"🍦{BEDANKT_EN_TOT_ZIENS}🍦\n")
