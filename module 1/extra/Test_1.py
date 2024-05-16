GETTALLEN_REEKS = [2,7,15,25, 76 , 57 , 94, 43 , 45, 20]
count = 0
def even_getallen (GETTALLEN_REEKS):
    if GETTALLEN_REEKS %2 == 1:
        return False
    else:
        return True 
    
even_getallen_1 = filter(even_getallen , GETTALLEN_REEKS)

for x in even_getallen_1:
    count +=1
    print(x)

print(f"{count} even nummers")

