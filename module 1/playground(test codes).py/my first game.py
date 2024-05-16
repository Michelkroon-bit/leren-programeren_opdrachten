
from colorama import Fore, Back, Style
import random
import colorama


#Initialize colorama
colorama.init(autoreset=True)
aantal_fout=0
bool_play = True
int_round= 1


while bool_play == True:
    int_var = 0
    print('round '+ str(int_round))
    int_random = random.randint (1,5) 
    while int_var < 5:
            #print(int_random)
            random_getal = int(input('vul een getal in tussen 1 en 5: '))
            if random_getal == int_random:
                print(Fore.GREEN + "Gefeliciteerd je hebt het getal goed geraden!")
                int_var = 5
            else:
                print(Fore.RED + "Jammer je hebt het getal niet goed geraden!")
                aantal_fout = aantal_fout +1
                int_var +=1 
    int_round+=1  # part of round while loop
    verder_spelen=input('wil je verder spelen ja of nee? ')
    if verder_spelen == 'ja':
        bool_play=True
        int_var=0
    else:
        bool_play=False
        
    
print(Fore.WHITE)        
print("aantal rondes gespeeld: " + str(int_round))
print("aantal foute antwoorden: "+ str(aantal_fout))
print('bedankt voor het spelen ;)')
