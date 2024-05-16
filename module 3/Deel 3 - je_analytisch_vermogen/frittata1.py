from recipe_lib import *
from frittata_ingredients import *
from math import ceil

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input('~Hoeveel mensen komen er eten?~ \n')) 

# ----- CALCULATIONS ----
# calculate factor 

factor = nr_persons / RECIPE_PERSONS

print(f'de factor is {factor}')

# calculate amount_eggs
amount_eggs = AMOUNT_EGGS * factor
eggs = round_piece(amount_eggs)
print(eggs)


# calculate amount_milk
amount_milk = AMOUNT_MILK * factor
milk = round_quarter(amount_milk)
print(milk)
# calculate amount_salt
amount_salt = AMOUNT_SALT * factor
salt = round_quarter(amount_salt)
print(salt)
# calculate amount_pepper = AMOUNT_MILK * factor
amount_pepper = AMOUNT_PEPPER * factor
pepper = round_quarter(amount_pepper)
print(pepper)
# calculate amount_oil
amount_oil = AMOUNT_OIL * factor
oil = round_quarter(amount_oil)
print(oil)

# calculate amount_onions
amount_onions = AMOUNT_ONIONS * factor
onions = round_piece(amount_onions)
print(onions)

# calculate amount_garlics
amount_garlics = AMOUNT_GARLICS * factor
garlics = round_piece(amount_garlics)
print(garlics)


# calculate amount_spinach
amount_spinach = AMOUNT_SPINACH * factor
spinach = round_quarter(amount_spinach)
print(spinach)


# calculate amount_paprikas
amount_paprikas = AMOUNT_PAPRIKAS * factor
paprikas = round_piece(amount_paprikas)
print(paprikas)
# calculate amount_cheese

amount_cheese = AMOUNT_CHEESE * factor
cheese = round_piece(amount_cheese)
print(cheese)
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print(f'* {eggs} {TXT_EGGS}')
print(f'* {milk} {UNIT_CUPS} {TXT_MILK}')
print(f'* {salt} {UNIT_TEASPOONS} {TXT_SALT}')
print(f'* {pepper} {UNIT_TEASPOONS} {TXT_PEPPER}')
print(f'* {oil} {UNIT_SPOONS} {TXT_OIL}')
print(f'* {onions} {TXT_ONIONS}')
print(f'* {garlics} {TXT_GARLICS}')
print(f'* {paprikas} {TXT_PAPRIKAS}')
print(f'* {spinach} {UNIT_CUPS} {TXT_SPINACH}')
print(f'* {cheese} {UNIT_CUPS} {TXT_CHEESE}')
print('-----------------------------------------------')