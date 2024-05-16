woorden =[] # lege lijst
    
for teller in range(5): #hoeveel keer repeat hij de vraag
    woord =(input(f'woord {teller+1}?'))# je laat de gebruiker hier een aantal woorden invullen doormiddel van input
    woorden.append(woord)# append staat voor voeg toe append voegt het woord wat je opgeschreven hebt achteraan de lijst toe
    
print(woorden)# print de lijst



#() noemen ze een tuple (kan niet aangepst worden)
#[] noemen ze een lijst (kan wel aangepast worden)






# alfabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# letter = input('type een leter uit het alfabet in')


# if letter.lower() in alfabet:
#     print(alfabet)
