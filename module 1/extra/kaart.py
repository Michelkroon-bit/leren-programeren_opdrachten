import random

kaarten = ["2" , "3" , "4" , "5" , "6" ,"7" ,"8" , "9" , "10" , "aas" , "boer" , "vrouw" , "heer"  ]
soort_kaart =["klaver" , "schoppen" , "ruiten" , "harten" ]
deck_kaarten=[]
overige_kaarten=[]
for x in kaarten:
    for b in soort_kaart:
        deck_kaarten.append(f"{b} {x}")

deck_kaarten.append("joker")
deck_kaarten.append("joker")
random.shuffle(deck_kaarten)

kaart = 0
for j in deck_kaarten:
    if kaart <7:
        kaart +=1
        print(f"kaart {kaart} {j}")
    else:
        overige_kaarten.append(j)
print("")
print(f"deck {len(overige_kaarten)} {overige_kaarten}")