from my_functions import *
from time import sleep


lijst_met_opties = ['A) getallen optellen', 'B) getallen aftrekken', 'C) getallen vermenigvuldigen', 'D) getallen delen', 'E) getal ophogen', 'F) getal verlagen','G) getal verdubbelen', 'H) getal halveren?']

def wat_wilt_u_doen():
    firstround = True
    print('wat wilt u doen')
    for x in lijst_met_opties:
        print (x)
    print('\n')
    choice = input('>> ')
    choice = choice.upper()

    if choice == 'A':
        print('getallen optellen')
        n1 = int(input('welk getal wilt u invullen: \n'))
        n2 = int(input(f'welk getal optellen bij {n1} \n'))
        uitkomst = addition(n1 , n2)
        print(f'{n1} + {n2} = {uitkomst}')
        print('-----------------------------------------')
        
    elif choice == 'B':
        print('getallen aftrekken')
        n1 = int(input('welk getal wilt u invullen: \n'))
        n2 = int(input(f'welk getal optellen bij {n1} \n'))
        uitkomst = substraction(n1 , n2)
        print(f'{n1} - {n2} = {uitkomst}')
        print('-----------------------------------------')
        
    elif choice == 'C':
        print('getallen vermenigvuldigen')
        n1 = int(input('welk getal wilt u invullen: \n'))
        n2 = int(input(f'welk getal optellen bij {n1} \n'))
        uitkomst = multiplication(n1 , n2)
        print(f'{n1} * {n2} = {uitkomst}')
        print('-----------------------------------------')
    
    elif choice == 'D':
        print('getallen delen')
        n1 = int(input('welk getal wilt u invullen: \n'))
        n2 = int(input(f'welk getal optellen bij {n1} \n'))
        uitkomst = division(n1 , n2)
        print(f'{n1} : {n2} = {uitkomst}')
        print('-----------------------------------------')
    
    elif choice == 'E':
        print('getallen ophogen')
        n1 = int(input('welk getal wilt u invullen: \n'))
        uitkomst = n1 + 1
        print(f'{n1} + 1 = {uitkomst}')
        print('-----------------------------------------')
    
    elif choice == 'F':
        print('getal verlagen')
        n1 = int(input('welk getal wilt u invullen: \n'))
        uitkomst = n1 - 1 
        print(f'{n1} - 1 = {uitkomst}')
        print('-----------------------------------------')
        
        
    elif choice == 'G':
        print('getal verdubbelen')
        n1 = int(input('welk getal wilt u invullen: \n'))
        uitkomst = n1 * 2
        print(f'{n1} x 2 = {uitkomst}')
        print('-----------------------------------------')
    
    elif choice == 'H':
        print('getal halveren')
        n1 = int(input('welk getal wilt u invullen: \n'))
        uitkomst = n1 / 2
        print(f'{n1} : 2 = {uitkomst}')
        print('-----------------------------------------')
    
    elif choice == '':
        if firstround == False:
            exit() 
    else:
        wat_wilt_u_doen()
        
wat_wilt_u_doen()