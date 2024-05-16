from fruitmand import *
from operator import itemgetter

sorted_list = sorted(fruitmand, key = lambda x: x["weight"] ,reverse=True)

for x in sorted_list:
    print(x['name'], x['weight'])



#In Python staat "lambda" voor een anonieme functies.