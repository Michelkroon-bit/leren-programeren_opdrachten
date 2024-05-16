getallen_lijst = []
while True:
    print("vul een getal in of type 'quit' om te stoppen")
    getal = input(">> ")
    if getal == 'quit':
        break
    else:
        getal = int(getal)
        getallen_lijst.append(getal)
        som = sum(getallen_lijst)
print(som)