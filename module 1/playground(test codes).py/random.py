import random

favoritefood = input('wat is je favorite eten ')
trueorFalse= random.randint(0,3)

if trueorFalse == 0:
    print ('dat lust ik niet')

elif trueorFalse == 1:
    print ('dat vind ik niet zo lekker')

elif trueorFalse == 2:
    print ('dit vind ik ook erg lekker')
    
elif trueorFalse == 3:
    print ('dat vind ik ook heel erg lekker')
