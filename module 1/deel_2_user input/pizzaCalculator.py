#michel kroon 
#opdracht:pizzacalculator

#constanten
KLEINE_PIZZA = 3.55
MEDIUM_PIZZA = 5.99
LARGE_PIZZA =  10.99

#user_input
print('Welkom bij onze bezorg service')
pizzaS = int(input("hoeveel kleine pizza's wilt u bestellen "))
pizzaM= int(input("hoeveel medium pizza's wilt u bestellen "))
pizzaL= int(input("hoeveel large pizza's wilt u bestellen "))

#rekensom variable keer constanten
PizzaS=pizzaS*KLEINE_PIZZA
PizzaM=pizzaM*MEDIUM_PIZZA
PizzaL=pizzaL*LARGE_PIZZA

#rekkensom plus afronden
totaal_in_float=PizzaS+PizzaM+PizzaL
totaal=int(round(totaal_in_float,2))


#bonnetje 
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print('****************************************************************************************************************|')
print(f" | producten die u besteld heeft: {pizzaS} kleine pizza's , {pizzaM} medium pizza's en {pizzaL} large pizza's                        |")
print(" |                                                                                                              |")
print(f" | het totaal is: {totaal} euro                                                                                       |")
print(" | bedankt voor uw bestelling                                                                                   |")
print("****************************************************************************************************************|")
























print('gemaakt door michel kroon')