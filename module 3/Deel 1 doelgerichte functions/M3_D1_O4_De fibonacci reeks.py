def De_fibonacci_reeks(herhaal):
    x = 0
    getal1 = 0
    getal2 = 1
    lijst = [getal1 , getal2]
    while x <= herhaal:
        uitkomst = getal1 + getal2
        getal1 = getal2
        getal2 = uitkomst
        x += 1
        lijst.append(uitkomst)
    print(lijst)
    return uitkomst


De_fibonacci_reeks(7)