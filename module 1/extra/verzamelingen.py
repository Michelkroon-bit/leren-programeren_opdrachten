
mijn_tuple= ()#voorbeeld van tuple kan NIET aangepast worden
 #voorbeeld van een dictionairy
auto_lijst= []#voorbeeld van lijst
 
for x in range (2):
    auto= {}
    auto["merk"] = input("Wat is het type auto ")
    auto["model"] = input("Wat is het model auto ")
    auto["prijs"] = int(input("wat is de prijs voor de auto "))
    auto_lijst.append(auto)

for x in auto_lijst:
    print(x["prijs"])
