DOOS_12= 12
DOOS_6 = 6


aantal_eieren = int(input('hoeveel eieren moet ik pakken '))

dozen_12 = aantal_eieren // DOOS_12
print(dozen_12)

rest = aantal_eieren % DOOS_12
print(rest)

print (f'u moet {dozen_12} dozen van 12 hebben en {rest} dozen van 6 ')