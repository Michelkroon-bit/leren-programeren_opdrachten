from colorama import Fore

# --> Constanten <--#
PIZZAS = [{"name":'kleine' , 'price':5.50 , 'amount': 0 } , {"name":'middel' , 'price':7.50 , 'amount': 0} ,{"name":'grote' , 'price':12.00 , 'amount': 0}]
BTW_GEHALTE = 21

#alle user_input functies kunnen in 1 functie gezet worden  



uiteindelijke_bestelling = []
print(''' ____                   
/    \			
  u  u|      _______    
    \ |  .-''#%&#&%#``-.   
   = /  ((%&#&#&%&#%&%&))  
    |    `-._#%&##&%_.-'   
 /\/\`--.   `-."".-'
 |  |    \   /`./          
 |\/|  \  `-'  /
 || |   \     /            

''')

print('🍕Welkom bij de pizzaria mag ik uw bestelling alstublieft?🍕 \n')



def user_input(pizza):
    while True:
        try:
            pizza['amount'] = int(input(f"Hoeveel {pizza['name']} pizza's? \n"))
            if pizza['amount'] <0:
                print('je moet wel een getal boven de nul invullen.')
            else:
                break
            
        except ValueError:
            print('je moet wel een getal invullen. ')
    return pizza

for pizza in PIZZAS:
    user_input(pizza)

totaal = 0

print('**************Pizzaria**************')


# --> Roep alle user_input functies aan <-- #
for pizza in PIZZAS:
    totaal += pizza['amount'] * pizza['price']
    print(f"|Prijs {pizza['name']} pizza's: {pizza['amount'] * pizza['price']} Euro    |")
print('|----------------------------------|')
print(f'|                    Btw prc:   {BTW_GEHALTE}%|')
print(f'|                    Totaal: €{totaal}')
print('------------------------------------')
print(Fore.RED + 'bedankt voor het bestellen bij pizzaria')


#gebruikt gemaakt van 
#dict
#functies
#lijsten
#forloop
