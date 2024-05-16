#functie 1 (laat met rust)
def naam_en_leeftijd_invullen() -> dict:
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    return {'namen':name , 'leeftijd' :age}
    
#functie 2     
def meer_namen_toevoegen ():
    lijst_dict = []
    while True:
        print('druk op "ENTER" om door te gaan of type "STOP" om te printen. ')
        nog_een_naam_toevoegen = input('>> ')
        if nog_een_naam_toevoegen == '':
            lijst_dict.append(naam_en_leeftijd_invullen())
        else:
            
            break
    return(lijst_dict)


alle_namen = [naam_en_leeftijd_invullen()] + meer_namen_toevoegen()
for x in alle_namen:
    print(f"{x['namen']} is {x['leeftijd']} jaar oud")

