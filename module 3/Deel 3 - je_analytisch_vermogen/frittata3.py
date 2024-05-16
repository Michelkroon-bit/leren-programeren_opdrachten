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


# calculate amount_milk
amount_milk = AMOUNT_MILK * factor
milk = round_quarter(amount_milk)

# calculate amount_salt
amount_salt = AMOUNT_SALT * factor
salt = round_quarter(amount_salt)

# calculate amount_pepper = AMOUNT_MILK * factor
amount_pepper = AMOUNT_PEPPER * factor
pepper = round_quarter(amount_pepper)

# calculate amount_oil
amount_oil = AMOUNT_OIL * factor
oil = round_quarter(amount_oil)


# calculate amount_onions
amount_onions = AMOUNT_ONIONS * factor
onions = round_piece(amount_onions)


# calculate amount_garlics
amount_garlics = AMOUNT_GARLICS * factor
garlics = round_piece(amount_garlics)



# calculate amount_spinach
amount_spinach = AMOUNT_SPINACH * factor
spinach = round_quarter(amount_spinach)



# calculate amount_paprikas
amount_paprikas = AMOUNT_PAPRIKAS * factor
paprikas = round_piece(amount_paprikas)

# calculate amount_cheese

amount_cheese = AMOUNT_CHEESE * factor
cheese = round_piece(amount_cheese)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print(f'* {eggs} {str_single_plural(eggs , TXT_EGGS)}')
print(f'* {str_amount_fraction(milk)} {str_single_plural(milk , TXT_CUPS)} {TXT_MILK} ({unit2ml(milk , ML_CUP)} ml )')
print(f'* {str_amount_fraction(salt)} {str_single_plural(salt , TXT_TEASPOONS)} {TXT_SALT}  ({ml2gram(unit2ml(salt , ML_TEASPOON),GRAM_PER_ML_SALT)} gram) ')
print(f'* {str_amount_fraction(pepper)} {str_single_plural(pepper , TXT_TEASPOONS)} {TXT_PEPPER}({ml2gram(unit2ml(pepper , ML_TEASPOON),GRAM_PER_ML_PEPPER)} gram)')
print(f'* {str_amount_fraction(oil)} {str_single_plural(oil , TXT_SPOONS)} {TXT_OIL} ({unit2ml(oil , ML_SPOON)} ml )')
print(f'* {onions} {str_single_plural(onions , TXT_ONIONS)}')
print(f'* {garlics} {str_single_plural(garlics ,TXT_GARLICS)}')
print(f'* {paprikas} {str_single_plural(paprikas,TXT_PAPRIKAS)}')
print(f'* {str_amount_fraction(spinach)} {str_single_plural(spinach , TXT_CUPS)} {TXT_SPINACH} ({ml2gram(unit2ml(spinach , ML_CUP),GRAM_PER_ML_SPINACH)} gram)')
print(f'* {str_amount_fraction(cheese)} {str_single_plural(cheese , TXT_CUPS)} {TXT_CHEESE} ({ml2gram(unit2ml(cheese , ML_CUP),GRAM_PER_ML_CHEESE)} gram)')

print('-----------------------------------------------')

# str_amount_fraction
# str_single_plural