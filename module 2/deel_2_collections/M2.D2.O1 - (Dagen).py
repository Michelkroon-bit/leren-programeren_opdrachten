#tuple 
dagen = ("maandag" , "dinsdag" , "woensdag" , "donderdag" , "vrijdag" , "zaterdag" , "zondag")

for index in range(7):
    print(dagen[index])
# print(f"de weekdagen zijn:{weekdagen}")
print("")
for index in range (5,7):
    print(dagen[index])
print("")
for index in range (4 , -1 , -1):
    print(dagen[index])
print("")
for dag in dagen:
    print(dag)
    

    
print("")

werkdagen = dagen[0 : 5]
print(f"de werkdagen zijn:{werkdagen}")

print("")

weekenddagen = dagen[5 : 7]
print(f"de weekend dagen zijn :{weekenddagen}")

print("")

weekenddagenreversed=list(dagen[5:7])
weekenddagenreversed.reverse()
print(f"de weekenddagen achterstevoren zijn :{weekenddagenreversed}")

print("")

werkdagenreversed=list(dagen[0:5])
werkdagenreversed.reverse()
print(f"de werkdagen achterstevoren zijn :{werkdagenreversed}")






# weekenddagenreversed = dagen[-2:][::-1]
# print(f"de weekenddagen achterstevoren zijn :{weekenddagenreversed}")

# print("")

# werkdagenreversed = dagen[:5][::-1]
# print(f"de werkenddagen achterstevoren zijn :{werkdagenreversed}")
