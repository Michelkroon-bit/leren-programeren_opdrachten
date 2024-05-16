from fruitmand import *
fruitmand.append({"name":"watermeloen" , "weight":2500 })

totaal = 0
for x in fruitmand:
    totaal += x["weight"]

print(f'Het totale gewicht van de fruitmand is {str(totaal)} gram of {str(totaal / 1000)} kilogram.')

