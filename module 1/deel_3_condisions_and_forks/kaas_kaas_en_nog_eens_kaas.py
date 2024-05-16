print('start')
start_spel=input('is de kaas geel? ')
if start_spel == 'ja':
    prijs =input('is de kaas belachelijk duur? ')
    if prijs== 'ja':
        print('emmelthaler')
    elif prijs == 'nee':
        hard_als_steen=input('is de kaas hard als steen? ')
        if hard_als_steen == 'ja':
            print('parmigano reggiano')
        elif hard_als_steen == 'nee':
            print('goudse kaas')
elif start_spel == 'nee':
    schimmel=input('heeft de kaas blauwe schimmel ')
    if schimmel == 'ja':
        korst = input('heeft de kaas korst? ' )
        if korst == 'ja':
            print('blue de rochbaron')
        elif korst == 'nee':
            print("foume d'ambert")
    elif schimmel == "nee":
        korst = input('heeft de kaas korst? ' )
        if korst == 'ja':
            print('cambert')
        elif korst == 'nee':
            print("mazzarella")


# feedback alle nee antwoorden kunnen ook veranderen in een elif of else