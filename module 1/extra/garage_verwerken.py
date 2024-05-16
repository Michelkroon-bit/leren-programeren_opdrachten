from garage import auto_lijst

print (f"ik heb {len(auto_lijst)} auto's in mijn garage")

aantal_autos=0
for auto in auto_lijst:
    if auto['merk'] == "Toyota":
        aantal_autos +=1
        print(auto['merk'])
print(aantal_autos)

#mijn oplossing
print('mijn oplossing')

sorted_list = sorted(auto_lijst, key = lambda x: x["motorinhoud"] ,reverse=False)
for x in sorted_list:
    print(f' merk = {x["merk"] }, motorinhoud = {x["motorinhoud"]}')
    
print('')   
    
#ander oplossing
print("andere oplossing")

print('min')
def get_motor_inhoud(a):
    return(a['motorinhoud'])

print(min(auto_lijst, key= get_motor_inhoud))
print('')
# max oplossing
print('max')
def get_motor_inhoud(a):
    return(a['motorinhoud'])

print(max(auto_lijst, key= get_motor_inhoud))


