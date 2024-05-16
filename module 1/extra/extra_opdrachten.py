lijst = []
while True:
    naam = input("vul een naam in ")
    if naam == "stop":
        break
    lijst.append(naam)
print(lijst)

for x in lijst:
    print(x)