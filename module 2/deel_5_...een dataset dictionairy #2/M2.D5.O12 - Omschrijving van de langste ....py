from fruitmand import fruitmand

#gestorteerde lengte van de naam
sorted_list = sorted(fruitmand, key = lambda x: len(x["name"]) ,reverse=True)
langste_naam = sorted_list[0]
kleur_translated = ''

#kleuren vertaling
if langste_naam['color'] == 'orange':
    kleur_translated = 'oranje'
elif langste_naam['color'] == 'yellow':
    kleur_translated = 'gele'
elif langste_naam['color'] == 'green':
    kleur_translated = 'groene'
elif langste_naam['color'] == 'red':
    kleur_translated = 'rode'
elif langste_naam['color'] == 'brown':
    kleur_translated = 'bruine'
elif langste_naam['color'] == 'pink':#toegevoegd
    kleur_translated = 'roze'
elif langste_naam['color'] == 'black':#toegevoegd
    kleur_translated = 'zwarte'
elif langste_naam['color'] == 'purple':#toegevoegd
    kleur_translated = 'paarse'
#eind output
print(f'De "{langste_naam["name"]}" ({len(langste_naam["name"])} letters) heeft een {kleur_translated} kleur en heeft een gewicht van {langste_naam["weight"]/1000} kg.' )

