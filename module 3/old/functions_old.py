from data import *
import sys
import time

import sys
import time
from colorama import init
from termcolor import colored

# Initialiseer colorama


# Voorbeeld gebruik


def typemachine_print (prompt):
    for x in prompt:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    return prompt

# def vraag_voor_particulier_of_zakelijk ():
#     typemachine_print('Bent u \n1) een particuliere klant of \n2) een zakelijke klant?')


#--> vraag om hoeveelheid bolletjes <--#
def vraag_hoeveel_bolletjes () -> int:
    while True:
        try:
            typemachine_print('hoeveel bolletjes ijs wilt u hebben?\n')
            hoeveel_bolletjes = int(input())
            if hoeveel_bolletjes >= 1 and hoeveel_bolletjes <= 8:
                return hoeveel_bolletjes
            
            elif hoeveel_bolletjes < 1:
                typemachine_print(f"{U_MOET_WEL_EEN_GETAL_BOVEN_DE_0_INVOEREN}\n")
                
            else:
                typemachine_print(f"{SORRY_ZULKE_GROOTTE_BAKJES_VERKOPEN_WIJ_NIET}\n")
        except ValueError:
            typemachine_print('Je moet wel een getal invullen\n')


def get_hoorntje_of_bakje(hoeveel_bolletjes):
    while True:
        if hoeveel_bolletjes >=1 and hoeveel_bolletjes <=3:
            typemachine_print(f"Wilt u deze {hoeveel_bolletjes} bolletje(s) in een hoorntje of een bakje?\n")
            keuze = input()
            
            if keuze.lower() in ("hoorntje" , "bakje"):

                return keuze.lower() 
                    
            else:
                typemachine_print(f"{SORRY_IK_BEGRIJP_HET_NIET}\n")
        

        elif hoeveel_bolletjes >=4 and hoeveel_bolletjes <=8:
            return 'bakje'
        else:
            print(SORRY_IK_BEGRIJP_HET_NIET)


def get_smaken(int_aantal_bolletjes) :
    smaken_lijst =[]
    keuze = 1
    while keuze <= int_aantal_bolletjes:
        typemachine_print(f'Welke smaak wilt u voor bolletje nummer {keuze}? \nA) Aardbei \nC) Chocolade \nM) Munt \nV) Vanille?\n')
        welke_smaak_wilt_u = input("")
        
        if welke_smaak_wilt_u.upper() == "A":
            smaken_lijst.append("Aardbei")
            keuze +=1 
            
        
        elif welke_smaak_wilt_u.upper() == "C":
            smaken_lijst.append("Chocolade")
            keuze +=1 
            
        
        elif welke_smaak_wilt_u.upper() == "M":
            smaken_lijst.append("Munt")
            keuze +=1 
            
        elif welke_smaak_wilt_u.upper() == "V":
            smaken_lijst.append("Vanille")
            keuze +=1 
            
        else:
            print(SORRY_IK_BEGRIJP_HET_NIET)

        
        
    return smaken_lijst
    

#--> check of je moet vragen om een bakje of hoorntje of als je een bakje moet geven <--#



def get_toppings(int_aantal_bolletjes):
    
    typemachine_print(f'Wat voor topping wilt u: \nA) Geen \nB) Slagroom \nC) Sprinkels  \nD) Caramel Saus \n')
    welke_topping_wilt_u = input("")
    if welke_topping_wilt_u.upper() == "A":
        typemachine_print('Geen toppings dus oke..')
        return ""

    elif welke_topping_wilt_u.upper() == "B":
        return "Slagroom"
        
    elif welke_topping_wilt_u.upper() == "C":
        return "Sprinkels"
        
    elif welke_topping_wilt_u.upper() == "D":
        return "Caramel Saus"
    else:
        typemachine_print(SORRY_IK_BEGRIJP_HET_NIET)

# -->voeg alle values uit de functies hierboven toe als dict aan de lijst <--#
def get_bestelling ():
    hoeveel_bolletjes = vraag_hoeveel_bolletjes()
    get_hoorntje = get_hoorntje_of_bakje(hoeveel_bolletjes)
    welke_smaken = get_smaken(hoeveel_bolletjes)
    get_topping = get_toppings(hoeveel_bolletjes)
    bestelde_items = {
    "ijsje": hoeveel_bolletjes ,
    "bakje/hoorntje": get_hoorntje,
    "smaak": welke_smaken,
    "topping": get_topping
    }
    return bestelde_items
