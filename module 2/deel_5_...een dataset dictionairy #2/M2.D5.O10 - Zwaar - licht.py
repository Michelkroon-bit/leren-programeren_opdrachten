from fruitmand import *
from operator import itemgetter

sorted_list = sorted(fruitmand, key = lambda x: x["weight"] ,reverse=True)

for x in sorted_list:
    print(f"{x['name']}, {x['weight']} gram")



#In Python staat "lambda" voor een anonieme functies.