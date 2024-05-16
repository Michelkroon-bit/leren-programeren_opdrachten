from fruitmand import *
from operator import itemgetter

sorted_list = sorted(fruitmand, key = lambda x: x["weight"] ,reverse=True)
for x in sorted_list:
    print(f"{x['name']}, {x['weight']/1000}kg")



#In Python staat "lambda" voor een anonieme functies.