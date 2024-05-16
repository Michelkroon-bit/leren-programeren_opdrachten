def naam_en_leeftijd_invullen() -> dict:
    print("welkom bij deze functie u gaat nu uw naam en leeftijd invullen")
    name = input('vul uw naam in: ').capitalize()
    age = int(input('vul uw leeftijd in: '))
    return {'naam':name , 'leeftijd' :age}
    
ingevulde_naam = naam_en_leeftijd_invullen()

print(f'{str(ingevulde_naam["naam"])} is {ingevulde_naam["leeftijd"]} jaar oud')


