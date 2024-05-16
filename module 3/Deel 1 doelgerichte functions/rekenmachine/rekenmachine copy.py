from my_functions import *

from time import sleep

def opties():
    lijst_met_opties = ['A) getallen optellen', 'B) getallen aftrekken', 'C) getallen vermenigvuldigen', 'D) getallen delen', 'E) getal ophogen', 'F) getal verlagen','G) getal verdubbelen', 'H) getal halveren?']

    for x in lijst_met_opties:
        print (x)
    print('\n')
    choice = input('>> ')
    choice = choice.upper()
    return choice



def wat_wilt_u_doen(parameter_uitkomst):
    
    if type(parameter_uitkomst) == str:
        firstround = True
    else:
        firstround = False
    
    
    if parameter_uitkomst == '':
        print('Wat wilt u doen: ')
        choice = opties()
        n1 = float(input('welk getal wilt u invullen: \n'))
        
    
    else:
        print(f'Wat wilt u met {parameter_uitkomst} doen: ')
        n1 = parameter_uitkomst
        choice = opties()
        
        
        #A
    if choice == 'A':
        print('getallen optellen')
        n2 = float(input(f'welk getal optellen bij {n1} \n'))
        uitkomst = addition(n1 , n2)
        print(f'{n1} + {n2} = {uitkomst}')
   
        #B
    elif choice == 'B':
        print('getallen aftrekken')
        n2 = float(input(f'welk getal aftrekken bij {n1} \n'))
        uitkomst = substraction(n1 , n2)
        print(f'{n1} - {n2} = {uitkomst}')
       
        #C
    elif choice == 'C':
        print('getallen vermenigvuldigen')
        n2 = float(input(f'welk getal vermenigvuldigen bij {n1} \n'))
        uitkomst = multiplication(n1 , n2)
        print(f'{n1} * {n2} = {uitkomst}')
       
        #D
    elif choice == 'D':
        print('getallen delen')
        n2 = float(input(f'welk getal delen bij {n1} \n'))
        uitkomst = division(n1 , n2)
        print(f'{n1} : {n2} = {uitkomst}')
        
        #E
    elif choice == 'E':
        print('getallen ophogen')
        n2 = 1
        uitkomst = n1 + n2
        print(f'{n1} + 1 = {uitkomst}')

        #F
    elif choice == 'F':
        print('getal verlagen')
        n2 = 1
        uitkomst = n1 - n2 
        print(f'{n1} - 1 = {uitkomst}')
 
        #G
    elif choice == 'G':
        print('getal verdubbelen')
        n2 = 2
        uitkomst = n1 * n2
        print(f'{n1} x 2 = {uitkomst}')

        #H
    elif choice == 'H':
        print('getal halveren')
        n2 = 2
        uitkomst = n1 / n2
        print(f'{n1} : 2 = {uitkomst}')

    elif choice == '':
        if firstround == False:
            print('programma stopt')
            sleep(1)
            exit() 
    else:
        wat_wilt_u_doen()  
    
    return uitkomst

uitkomst = ''
while True:
    uitkomst = wat_wilt_u_doen(uitkomst)