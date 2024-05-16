from fruitmand import fruitmand

#gestorteerde lengte van de naam
sorted_list = sorted(fruitmand, key = lambda x: len(x["name"]) ,reverse=True)
fruit_met_langste_naam = sorted_list[0]
kleur_translated = ''

kleuren = {'orange': 'oranje', 'yellow':'gele','green':'groene' , 'red':'rode', 'brown':'bruine'}

#kleuren vertaling

#eind output
print(f'De "{fruit_met_langste_naam["name"]}" ({len(fruit_met_langste_naam["name"])} letters) heeft een {kleuren[fruit_met_langste_naam["color"]]} kleur en heeft een gewicht van {fruit_met_langste_naam["weight"]/1000} kg of {fruit_met_langste_naam["weight"]} gram.' )

