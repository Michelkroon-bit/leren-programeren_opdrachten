import random

#selecteer 2 nummers
num1 = (random.randint(1,10))
num2 = (random.randint(5,15))

#vraag om een antwoord

number = input(f'Weet jij wat {num1} + {num2} is? ')
try:
#geef reactie op het antwoord

    if (number == num1+num2):
        print('Dat is juist')
    elif (number != num1+num2):
        print('Nee dat klopt niet')
except:
    print('Dat is geen nummer!')
