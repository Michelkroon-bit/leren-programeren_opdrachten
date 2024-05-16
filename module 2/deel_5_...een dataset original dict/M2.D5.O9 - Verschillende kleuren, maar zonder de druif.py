from fruitmand import *
#fruitmand.append({"name":"watermeloen" , "weight":2500 })

index = 0
for dict in fruitmand: 
    if dict['name'] =='druif':
        fruitmand.pop(index)
    print(dict['color'])
    index += 1
for x in fruitmand:
    print(x)
    
    
# for x in fruitmand:
#     print(x)


