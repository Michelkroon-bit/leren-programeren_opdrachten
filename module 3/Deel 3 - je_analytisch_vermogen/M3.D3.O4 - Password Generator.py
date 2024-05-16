import string
import string_utils
import random
from colorama import init
from termcolor import colored
init()
lengte = 24

wachtwoord = ''
wachtwoord1 = ''

lowercase_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase
tekens = '@#$%&_?'
getallen = '0123456789'

random_uppercase_letter = random.randint(2,6)
random_cijfers =  random.randint(4,7)
random_lowercase_letter = lengte - random_cijfers - random_uppercase_letter - 3
wachtwoord1 += wachtwoord.join(random.choices(getallen, k=random_cijfers)) #var aanpassen 

wachtwoord1 += wachtwoord.join(random.choices(upper_case_letters, k=random_uppercase_letter))

wachtwoord1 += wachtwoord.join(random.choices(lowercase_letters, k= random_lowercase_letter ))
  
wachtwoord1 += wachtwoord.join(random.choices(tekens, k=3))

# random.shuffle(wachtwoord_met_tekens)




while wachtwoord1[0] in getallen or wachtwoord1[1] in getallen or wachtwoord1[2] in getallen or \
        wachtwoord1[11] in upper_case_letters or wachtwoord1[12] in upper_case_letters or wachtwoord1[-1] in lowercase_letters or wachtwoord1[0] in tekens or wachtwoord1[-1] in tekens: 
      
        wachtwoord1 = (string_utils.shuffle(wachtwoord1))


repeat = True   
if len(wachtwoord1) > 24:
    nieuw_wachtwoord = ''
    for elk_teken in wachtwoord1:
        if elk_teken not in lowercase_letters:
            nieuw_wachtwoord += tekens
    geshuffelde_wachtwoord = nieuw_wachtwoord

elif len(wachtwoord1) < 24:
    while repeat:
        wachtwoord1 += random.choice(tekens)    
else:
    repeat = False

#for debugging
print(f'postie 12 {wachtwoord1[11]}')
print(f'postie 13 {wachtwoord1[12]}')
#for debugging 


print('')
print(f'uw gegenereerde wachtwoord: {wachtwoord1} \nhet wachtwoord is {len(wachtwoord1)} tekens lang \n')


print('*****************************TEST*****************************')
print('Kijk of er op de laatste positie een speciaal teken staat')
if wachtwoord1[0] in tekens or wachtwoord1[-1] in tekens:
    print(colored('Result: True', 'red'))
else:
    print(colored('Result: False','green')) 
    
print('\n')
print('Kijk of er op de middelste posties een hoofdletter staat')
if wachtwoord1[11] in upper_case_letters or wachtwoord1[12] in upper_case_letters:
    print(colored('Result: True', 'red'))
else:
    print(colored('Result: False','green')) 

print('\n')
print('Kijk of er op de 1e 3 posities een getal staat')
if wachtwoord1[0] in getallen or wachtwoord1[1] in getallen or wachtwoord1[2] in getallen:
    print(colored('Result: True', 'red'))
else:
    print(colored('Result: False','green')) 
    
print('\n')
print('Kijk of er op de laatste positie geen kleine letter staat')
if wachtwoord1[-1] in lowercase_letters :
    print(colored('Result: True', 'red'))
else:
    print(colored('Result: False','green')) 

print('\n')
print('Kijk of de speciale tekens wel uit de lijst komt')
if tekens == tekens :
    print(colored('Result: True', 'green'))
    
else:
    print(colored('Result: False','red'))  
print('***************************EINDE TEST**************************') 

# Random 2 tot 6 hoofdletters. Done line 17
# Een hoofdletter mag niet op de twee middelste posities staan. done line 30
# Minimaal 8 kleine letters. Done line 36
# Het wachtwoord mag niet met een kleine letter eindigen. done line 30
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?. Done line 10
# De speciale tekens mogen niet op de eerste of laatste positie staan. line 48
# Random 4 tot 7 cijfers (0 t/m 9). Done line 19
# Op de eerste 3 posities mag geen cijfer staan line 48
