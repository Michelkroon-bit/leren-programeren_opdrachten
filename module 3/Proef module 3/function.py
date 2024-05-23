from data import *
import sys
import time
bestellingen_lijst = []

def typemachine_print (prompt):
    for x in prompt:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    return prompt

print('''         _
       ,' `,.
       >-.(__)
      (_,-' |
        `.  |
          `.|
            `''')


typemachine_print('🍦Welkom bij Papi Gelato je mag alle smaken kiezen zo lang het maar vanille ijs is🍦\n')

#--> vraag om hoeveelheid bolletjes <--#
def get_user_input ():
    while True:
        try:
            typemachine_print('hoeveel bolletjes ijs wilt u hebben? \n')
            hoeveel_bolletjes = int(input())
            if hoeveel_bolletjes >= 1 and hoeveel_bolletjes <= 8:
                return hoeveel_bolletjes
            
            elif hoeveel_bolletjes < 1:
                typemachine_print(f"{U_MOET_WEL_EEN_GETAL_BOVEN_DE_0_INVOEREN}\n")
                
            else:
                typemachine_print(f"{SORRY_ZULKE_GROOTTE_BAKJES_VERKOPEN_WIJ_NIET}\n")
        except ValueError:
            typemachine_print('Je moet wel een getal invullen\n')

#--> check of je moet vragen om een bakje of hoorntje of als je een bakje moet geven <--#
def get_hoorntje_of_bakje(hoeveel_bolletjes):
    if hoeveel_bolletjes >=1 and hoeveel_bolletjes <=3:
        typemachine_print(f"Wilt u deze {hoeveel_bolletjes} bolletje(s) in een hoorntje of een bakje?\n")
        keuze = input()
        
        if keuze.lower() in ("hoorntje" , "Hoorntje"):
            return "hoorntje"
        
        elif keuze.lower() in ("bakje" , "Bakje"):
            return"bakje"
        
        else:
            typemachine_print(f"{SORRY_IK_BEGRIJP_HET_NIET}\n")
    
    elif hoeveel_bolletjes >=4 and hoeveel_bolletjes <=8:
        return 'bakje'


# -->voeg alle values uit de functies hierboven toe als dict aan de lijst <--#
def get_bestelling ():
    user_input = get_user_input()
    get_hoorntje = get_hoorntje_of_bakje(user_input)
    
    bestelde_items = {
    "ijsje": user_input ,
    "bakje/hoorntje": get_hoorntje
    }
    
    bestellingen_lijst.append(bestelde_items)
    print('\n')
    typemachine_print(f"Uw bestelling is toegevoegd: een {get_hoorntje} met{user_input} bolletjes\n")
    print('\n')
    return bestellingen_lijst


# -->roep de functie aan<--#
maak_bestelling = get_bestelling()
while True:
    typemachine_print(f"Wilt u nog iets bestellen?\n")
    nog_iets_bestellen = input("")
    if nog_iets_bestellen in ('j','J','JA','ja','Ja'):
        get_bestelling()
    elif nog_iets_bestellen in ('N','n','NEE','nee','Nee'):
        print(f"🍦 {BEDANKT_EN_TOT_ZIENS} 🍦\n")
        break


#dit wordt het uitijndelijke bonnetje
print('---------------bonnetje---------------')
for x in maak_bestelling:
    print(f'{x["ijsje"]} bolletje(s) in een {x["bakje/hoorntje"]}')
print('--------------------------------------')
#print(maak_bestelling) #for debugging 