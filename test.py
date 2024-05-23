import os
import sys
import time
from coole_dingetjes import typemachine_print

bestellingen_lijst = []
BEDANKT_EN_TOT_ZIENS = 'Bedankt en tot ziens'
SORRY_IK_BEGRIJP_HET_NIET = 'Sorry ik begrijp het niet'
bestelling_count = 0

print('start programma')
time.sleep(1)
typemachine_print('Welkom bij Papi Gelato je mag alle smaken kiezen zo lang het maar vanille ijs is\n')

def bestel_progress():
    global bestelling_count
    bool_value = True
    while bool_value:
        bestelling_count += 1
        bestelling_string = f'bestelling {bestelling_count}'
        bestelling = {}
        
        typemachine_print("hoeveel bolletjes wilt u?\n")
        try: 
            hoeveel_bolletjes = int(input(""))
            if 1 <= hoeveel_bolletjes <= 3:
                typemachine_print(f"Wilt u deze {hoeveel_bolletjes} bolletje(s) in een hoorntje of een bakje?\n")
                hoorntje_of_bakje = input('').lower()
                if hoorntje_of_bakje == 'hoorntje':
                    bestelling[bestelling_string] = {'bolletjes': hoeveel_bolletjes, 'container': 'hoorntje'}
                    bestellingen_lijst.append(bestelling)
                    typemachine_print(f"Hier is uw hoorntje met {hoeveel_bolletjes} bolletjes\n")
                    bool_value = False
                elif hoorntje_of_bakje == 'bakje':
                    bestelling[bestelling_string] = {'bolletjes': hoeveel_bolletjes, 'container': 'bakje'}
                    bestellingen_lijst.append(bestelling)
                    typemachine_print(f"Hier is uw bakje met {hoeveel_bolletjes} bolletjes\n")
                    bool_value = False
                else:
                    typemachine_print(f"{SORRY_IK_BEGRIJP_HET_NIET}\n")
            elif 4 <= hoeveel_bolletjes <= 8:
                typemachine_print(f"Dan krijgt u van mij een bakje met {hoeveel_bolletjes} bolletjes\n")
                bestelling[bestelling_string] = {'bolletjes': hoeveel_bolletjes, 'container': 'bakje'}
                bestellingen_lijst.append(bestelling)
                bool_value = False
            elif hoeveel_bolletjes > 8:
                typemachine_print(f"Sorry, zulke grote bakken hebben we niet\n")
            else:
                typemachine_print(f"{SORRY_IK_BEGRIJP_HET_NIET}\n")
        except ValueError:
            typemachine_print('Je moet wel een getal invullen\n')

while True:
    bestel_progress()
    
    typemachine_print("Wilt u nog iets bestellen? (ja/nee)\n")
    nog_iets_bestellen = input("").lower()
    if nog_iets_bestellen in ('j', 'ja'):
        continue
    elif nog_iets_bestellen in ('n', 'nee'):
        typemachine_print(BEDANKT_EN_TOT_ZIENS + '\n')
        print(bestellingen_lijst)
        break
    else:
        typemachine_print(f"{SORRY_IK_BEGRIJP_HET_NIET}\n")
