# totaal = 0
# for x in range(1, 11):
#         totaal += x
#         print(x)
from time import sleep
artiesten = ['DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA', 'DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA','EMMINEM' ,'TUPAC', 'EMMINEM' , 'SNOOPDOG','EMMINEM' ,'TUPAC', 'EMMINEM' , 'SNOOPDOG','EMMINEM' ,'TUPAC', 'EMMINEM' , 'SNOOPDOG','EMMINEM' ,'TUPAC', 'EMMINEM' , 'SNOOPDOG' ]
groepeer_teller= {}

for a in artiesten:
        print(a)
        if a not in groepeer_teller:
                groepeer_teller[a]=0
                print(groepeer_teller)
        groepeer_teller[a] += 1
        print(groepeer_teller)
        sleep(4)

# localscoping = een locale variable die je alleen in een functie kan gebruiken 
# globalscoping = een variable die je overal in je file mag gebruiken