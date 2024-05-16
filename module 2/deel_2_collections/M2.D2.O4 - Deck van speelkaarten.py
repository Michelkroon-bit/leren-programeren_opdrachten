import random

aantal_kaarten=("2" , "3", "4", "5", "6", "7", "8", "9" ,"10" ,"boer" , "vrouw" , "koning" , "aas"  )
soort_kaarten=("klaver", "schoppen" , "ruiten" , "harten"  )
deck_kaarten = []
remaining_deck = []
   
for o in soort_kaarten:
    for b in aantal_kaarten :
        deck_kaarten.append(f"{o} {b}")
        
deck_kaarten.append("joker")
deck_kaarten.append("joker")
random.shuffle(deck_kaarten)

for x in range(1 , 8):
    kaart = deck_kaarten.pop(0)
    print(f"kaart {x} {kaart}  ")
print("")
print(f"deck ({len(deck_kaarten)} kaarten) {deck_kaarten}")