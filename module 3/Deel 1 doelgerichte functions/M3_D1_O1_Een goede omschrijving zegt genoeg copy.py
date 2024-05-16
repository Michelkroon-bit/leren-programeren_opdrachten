def delen_door_twee(getal:int) -> bool:
    return getal % 2 == 0
is_deelbaar_door_twee = delen_door_twee(getal = 6)# for debugging 
print(is_deelbaar_door_twee)




def draai_zin_om(ingevulde_zin:str) -> str:
    woorden = ingevulde_zin.split() #druif -> splits 
    omgekeerd = woorden[::-1]
    print(omgekeerd)#for debugging 
    omgekeerde_zin = ' '.join(omgekeerd)
    return omgekeerde_zin
omgedraaide_zin = draai_zin_om("1 2 3 4 5 6 7" )
print(omgedraaide_zin)




def characters_tellen(zinnetje_ingevuld:str) -> int:
    lijst_woorden = set(zinnetje_ingevuld)
    lengte_van_lijst_met_woorden = len(lijst_woorden)
    return lengte_van_lijst_met_woorden
zinnetje_ingevuld = characters_tellen('1234567') #telt aantal letters in een zin
print(zinnetje_ingevuld)




def gemiddelde_aantal_letters_van_woorden(gemaakte_zin:str) -> float:
    woorden = gemaakte_zin.split()#woorden
    
    count = 0
    for letter in woorden:#telt de aantal letters in de lijst met woorden
        count += len(letter)
    print(count)
    aantal_characters = count / len(woorden)
    return aantal_characters
aantal_characters = gemiddelde_aantal_letters_van_woorden('test 1234')#telt het aantal woorden
print(aantal_characters)


def tafels(de_tafel_van:int, hoevaak:int=10) -> None:
    for x in range(1, hoevaak+1):
        uitkomst = x * de_tafel_van
        print(f'{x} x {de_tafel_van} = {uitkomst}')
        
tafels(9, 15)# maakt de tafels van een ingevuld getal

