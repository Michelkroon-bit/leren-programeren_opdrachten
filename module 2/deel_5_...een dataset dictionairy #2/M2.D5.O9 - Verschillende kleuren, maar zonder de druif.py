from fruitmand import *
#fruitmand.append({"name":"watermeloen" , "weight":2500 })
index = 0
for x in fruitmand: 
    if x['name'] =='druif':
        fruitmand.pop(index)
    print(x['color'])
    index += 1
    
    
# for x in fruitmand:
#     print(x)
