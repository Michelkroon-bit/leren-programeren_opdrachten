import os
import sys
import time
from data import SORRY_IK_BEGRIJP_HET_NIET , BEDANKT_EN_TOT_ZIENS , bestellingen_lijst
# bestellingen_lijst = []
    


print('''         _
       ,' `,.
       >-.(__)
      (_,-' |
        `.  |
          `.|
            `''')


typemachine_print('🍦Welkom bij Papi Gelato je mag alle smaken kiezen zo lang het maar vanille ijs is🍦\n')


#--> input voor de hoeveelheid bolletjes <--#
def vraag_voor_hoeveel_bolletjes ():
    while True:
        try:
            typemachine_print("Hoeveel bolletjes wilt u?\n")
            aantal_bolletjes = int(input(""))
            if aantal_bolletjes >= 1:
                return aantal_bolletjes
            else:
                typemachine_print("Aantal bolletjes moet minimaal 1 zijn. Probeer het opnieuw.\n")
        except ValueError:
            typemachine_print("Je moet wel een getal invullen. Probeer het opnieuw.\n")


#--> vraag of de klant een bakje of een hoorntje wil en geef een error als er een ongeldige input gegeven wordr <--#
def vraag_bakje_of_hoorntje(aantal_bolletjes):
    while True:
        typemachine_print(f"Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?\n")
        hoorntje_of_bakje = input('').lower()
        if hoorntje_of_bakje in ('hoorntje', 'bakje'):
            return hoorntje_of_bakje
        else:
            typemachine_print("Ongeldige keuze. Kies alstublieft uit de keuze 'hoorntje' of 'bakje'.\n")

#zet logica bij elkaar van de 1e 2 ifs uit bestell progress


#--> voeg de uitijdelijke  bestelling toe aan de lijst van dictionairies <--#
def voeg_bestelling_toe(bestellingen_lijst, bestelling):
    typemachine_print(f"Uw bestelling is toegevoegd: {bestelling}\n")
    bestellingen_lijst.append(bestelling)
    print(bestellingen_lijst)
    return bestellingen_lijst


#--> alle if statements op basis van de  1e user input (dit staat in 1 functie omdat het voor mijn gevoel anders te rommelig werd) <--#


#potentiele aanpassing (pas deze functie aan) (als je extra tijd heb)
def bestel_progress(bestellingen_lijst):
    while True:
        aantal_bolletjes = vraag_voor_hoeveel_bolletjes()
        
        if 1 <= aantal_bolletjes <= 3:
            hoorntje_of_bakje = vraag_bakje_of_hoorntje(aantal_bolletjes)
            bestelling = {'bolletjes': aantal_bolletjes, 'bakje/hoorntje': hoorntje_of_bakje}
            typemachine_print(f"Hier is uw {hoorntje_of_bakje} met {aantal_bolletjes} bolletje(s)\n")
        
        elif 4 <= aantal_bolletjes <= 8:
            typemachine_print(f"Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes\n")
            bestelling = {'bolletjes': aantal_bolletjes, 'bakje/hoorntje': 'bakje'}
        
        elif aantal_bolletjes > 8:
            typemachine_print("Sorry, zulke grote bakken hebben we niet\n")
            return bestellingen_lijst
        
        else:
            typemachine_print(SORRY_IK_BEGRIJP_HET_NIET + "\n")
        
        bestellingen_lijst = voeg_bestelling_toe(bestellingen_lijst, bestelling)
        break
    
    return bestellingen_lijst


#--> vraag of de klant nog iets wilt bestellen <--#
# --> https://realpython.com/if-name-main-python/ dit uitzoeken <-- # 
while True:
    bestellingen_lijst = bestel_progress(bestellingen_lijst)
    typemachine_print(f" wilt u nog iets bestellen? ")
    nog_iets_bestellen = input("")
    if nog_iets_bestellen in ('j','J','JA','ja','Ja'):
        pass
    elif nog_iets_bestellen in ('N','n','NEE','nee','Nee'):
        typemachine_print(f"{BEDANKT_EN_TOT_ZIENS}\n")
        break

print(f"uw bestelling {bestellingen_lijst} \n")