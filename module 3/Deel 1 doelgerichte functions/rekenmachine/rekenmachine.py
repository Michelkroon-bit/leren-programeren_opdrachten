from my_functions import *

from time import sleep


lijst_met_opties = ['A) getallen optellen', 'B) getallen aftrekken', 'C) getallen vermenigvuldigen', 'D) getallen delen', 'E) getal ophogen', 'F) getal verlagen','G) getal verdubbelen', 'H) getal halveren?']


def wat_wilt_u_doen(parameter_uitkomst):
    
    global firstround
    
    if parameter_uitkomst == '':
        firstround = True
        print('Wat wilt u doen: ')
        for x in lijst_met_opties:
            print (x)
        print('\n')
        choice = input('>> ')
        choice = choice.upper()
    
    else:
        print(f'Wat wilt u met {parameter_uitkomst} doen: ')
        n1 = parameter_uitkomst
        for x in lijst_met_opties:
            print (x)
        print('\n')
        choice = input('>> ')
        choice = choice.upper()
        
        
        #A
    if choice == 'A':
        print('getallen optellen')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = float(input(f'welk getal optellen bij {n1} \n'))
        uitkomst = addition(n1 , n2)
        print(f'{n1} + {n2} = {uitkomst}')
        print('--------------------------')
        firstround = False
        return uitkomst
        
        
        #B
    elif choice == 'B':
        print('getallen aftrekken')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = float(input(f'welk getal aftrekken bij {n1} \n'))
        uitkomst = substraction(n1 , n2)
        print(f'{n1} - {n2} = {uitkomst}')
        print('--------------------------')
        firstround = False
        return uitkomst
        
        
        #C
    elif choice == 'C':
        print('getallen vermenigvuldigen')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = float(input(f'welk getal vermenigvuldigen bij {n1} \n'))
        uitkomst = multiplication(n1 , n2)
        print(f'{n1} * {n2} = {uitkomst}')
        print('--------------------------')
        firstround = False
        return uitkomst        
        
        
        #D
    elif choice == 'D':
        print('getallen delen')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = float(input(f'welk getal delen bij {n1} \n'))
        uitkomst = division(n1 , n2)
        print(f'{n1} : {n2} = {uitkomst}')
        print('--------------------------')
        firstround = False
        print(f'wat wil je met de uitkomst ({uitkomst}) doen?')
        return uitkomst
        
        
        #E
    elif choice == 'E':
        print('getallen ophogen')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = 1
        uitkomst = n1 + n2
        print(f'{n1} + 1 = {uitkomst}')
        print('--------------------------')
        firstround = False
        return uitkomst        
        
        
        #F
    elif choice == 'F':
        print('getal verlagen')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = 1
        uitkomst = n1 - n2 
        print(f'{n1} - 1 = {uitkomst}')
        print('--------------------------')
        firstround = False
        return uitkomst
        
        
        #G
    elif choice == 'G':
        print('getal verdubbelen')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = 2
        uitkomst = n1 * n2
        print(f'{n1} x 2 = {uitkomst}')
        print('--------------------------')
        firstround = False
        return uitkomst
        
        
        #H
    elif choice == 'H':
        print('getal halveren')
        if firstround == True:
            n1 = float(input('welk getal wilt u invullen: \n'))
        n2 = 2
        uitkomst = n1 / n2
        print(f'{n1} : 2 = {uitkomst}')
        print('--------------------------')
        firstround = False
        return uitkomst
    
    
    elif choice == '':
        if firstround == False:
            print('programma stopt')
            exit() 
    else:
        wat_wilt_u_doen()    

uitkomst = 0
firstround = True
while True:
    if firstround == True:
        uitkomst = wat_wilt_u_doen('')
    else:
        uitkomst = wat_wilt_u_doen(uitkomst)