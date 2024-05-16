from random import choice

kleuren = ("rood", "blauw", "groen", "geel" , "bruin")
hoeveel_snoepjes = int(input("hoeveel m&m's moeten er toegevoegd worden: ")) 

zak_met_MnMs = {"rood": 0 , "groen": 0 , "geel": 0 , "bruin": 0 , "blauw": 0}
#print(zak_met_MnMs["bruin"])


for x in range(hoeveel_snoepjes):
    mnm_kleur = choice(kleuren)
    zak_met_MnMs.update({mnm_kleur : zak_met_MnMs[mnm_kleur] + 1})

print(zak_met_MnMs)
    
    
    
    
# for x in range(hoeveel_snoepjes):
#     zak_met_MnMs.update({"kleur": choice(kleuren)})
# print(len(zak_met_MnMs))