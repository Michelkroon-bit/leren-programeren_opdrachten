gastheer_naam = ''

gastheer = input('is de gastheer aanwezig ')
if gastheer == 'ja': 
    gastheer_naam= input ('hoe heet de gastheer? ')    
    if gastheer_naam == 'ose':
        gastheer=False
    else:
        gastheer=True
    gastheer=True
else:
    gastheer=False

gasten = int(input('hoeveel gasten zijn er aanwezig? '))
if gasten  >= 4 and gasten <= 20:
    gasten=True
else:
    gasten=False

drank = input('is er drank aanwezig? ')
if drank =='ja':
    drank=True
else:
    drank=False

chips = input('is er chips aanwezig? ')
if chips == 'ja':
    chips = True   
else:
    chips=False
    
if gastheer and gasten and drank and chips == False:
    print('Start the Party')
elif chips and drank and gasten and gastheer == False:
    print('Start the Party')
elif chips and drank and gasten == False and gastheer:
    print('Start the party')
elif chips ==False and gasten ==False and drank and gastheer:
    print('Start the Party')
elif gastheer_naam == 'michel':
    print('Start the Party')

else:
    print('No Party')


#