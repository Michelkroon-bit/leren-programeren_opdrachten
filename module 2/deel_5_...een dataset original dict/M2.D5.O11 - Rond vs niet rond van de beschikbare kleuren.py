from fruitmand import *
kleuren = []#lijst met kleuren
for x in fruitmand:
    kleuren.append(x['color'])
    
# dups uit de lijst halen    
kleur_set = set(kleuren)
unique_kleuren = (list(kleur_set))

count_rond = 0 
count_not_rond = 0
while True:
    kleur_kiezen = input("kies een kleur uit de lijst  ")
    if kleur_kiezen not in unique_kleuren:
        print(f'De kleur {kleur_kiezen} zit er niet in de fruitmand')
    else:
        break 

for x in fruitmand: 
    if x['color'] == kleur_kiezen:   
        if x ['round']== True:
            count_rond +=1
        else:
            count_not_rond +=1
           
uitkomst_1 = count_rond - count_not_rond
#meer rond
if uitkomst_1 >0:
    print(f"Er zijn {uitkomst_1}  ronde vrucht(en) minder dan niet ronde vruchten in de kleur {kleur_kiezen}")

#minder rond
elif uitkomst_1 <0:
    print(f"Er zijn {abs(uitkomst_1)}  ronde vrucht(en) minder dan niet ronde vruchten in de kleur {kleur_kiezen}")
#gelijk
else:
    print(f'Er zijn {count_rond} ronde vruchten en {count_not_rond} niet ronde vruchten in de kleur {kleur_kiezen}')

