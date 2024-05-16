from collections import Counter
import math, random

# Gemiddelde berekenen
def gemiddelde_berekenen(som , aantal):
    gemiddelde = som / aantal
    return gemiddelde

# Som van alle getallen in de lijst
def opgetelde_sommen_van_lijst(getallen):
    som = sum(getallen)
    return som


# Het eerste getal in de lijst
def eerste_getal_in_lijst (getallen):
    eerste_getal = getallen[0]
    return eerste_getal

# Het kleinste getal gedeeld door het eerste controle getal
def delen_door_eerste_controle_getal(kleinste_getal , controlegetal1):
    delen1 = kleinste_getal / controlegetal1
    return delen1

# Het grootste getal gedeeld door het tweede controle getal
def gedeeld_door_tweede_controle_getal_1(grootste_getal , controlegetal2):
    delen2 = grootste_getal / controlegetal2
    return delen2

# alle unieke getallen
def unieke_getallen_selecteren(getallen):
    unieke_getallen = list(set(getallen))
    return unieke_getallen

 # Gemiddelde berekenen
def gemmideld_aantal (getallen):
    aantal = len(getallen)
    return aantal

# Het grootste getal in de lijst
def grootste_getal_in_lijst(getallen):
    grootste_getal = max(getallen)
    return grootste_getal

# Het kleinste getal in de lijst
def kleinste_getal_in_lijst(getallen):
    kleinste_getal = min(getallen)
    return kleinste_getal

# Aantal unieke elementen in de lijst
def aantal_elementen (getallen):
    aantal_elementen = len(getallen)
    return aantal_elementen

 # Verschil tussen aantal unieke elementen en eerste controle getal
def verschil_tussen_elementen(aantal_unieke_elementen , controlegetal1):
    verschil1 = abs(aantal_unieke_elementen - controlegetal1)
    return verschil1

# Sorteer de lijst van getallen
def elementen_in_gesorteerde_lijst(getallen):
    gesorteerde_lijst = sorted(getallen)
    return gesorteerde_lijst

# Sorteer de lijst van unieke getallen
def gesorteerde_lijst (getallen):
    gesorteerde_lijst_uniek = sorted(getallen)
    return gesorteerde_lijst_uniek

 # Tel het aantal keren dat elk uniek element voorkomt in de lijst
def elementen_tellen(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

    # Getallen die deelbaar zijn door het eerste controlle getal
def getallen_deelbaar_door_acht (getallen):
    deelbaar1 = []
    for getal in getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return deelbaar1


    # Getallen die deelbaar zijn door het tweede controlle getal
def deelbaar_door_tweede_controle_getal(unieke_getallen):
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return deelbaar2


    # Controleer of een bepaald getallen in de lijst voorkomen
def komt_voor_in_bepaalde_lijst(getallen):
    komtvoor = controlegetal1 in getallen and controlegetal2 in getallen
    return komtvoor


    # Vindt de posities van heteerste controle getal
def vind_posities_van_eerste_getal(getallen):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

    # Standaardafwijking berekenen
def bereken_standaardafwijking(gemiddelde , getallen , aantal):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

    # Shuffle de lijst
def shuffle_de_lijst(getallen):
    geshuffelde_lijst =random.shuffle(getallen)
    return geshuffelde_lijst

 # Verschil tussen twee getallen
def verschil_tussen_getallen(random_getal):
   verschil2 = abs(random_getal - controlegetal2)
   return verschil2


 # Pak een random getal uit de lijst
def random_getal_uit_lijst(getallen , aantal):
    random_getal = getallen[random.randint(0,aantal-1)]
    return random_getal

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

    #je hoeft geen extra functies te schrijven voor uitrekenprogramma's met ingebouwde functies zoals len,min,max,sum    

    resultaten = {
        "Aantal getallen": len(getallen),
        "Gemiddelde": gemiddelde_berekenen(opgetelde_sommen_van_lijst(getallen), len(getallen)),
        "Som": opgetelde_sommen_van_lijst(getallen),
        "Grootste getal": grootste_getal_in_lijst(getallen),
        "Kleinste getal": kleinste_getal_in_lijst(getallen),
        "Eerste getal": eerste_getal_in_lijst(getallen),
        f"{kleinste_getal_in_lijst(getallen)} / {controlegetal1}": delen_door_eerste_controle_getal(kleinste_getal_in_lijst(getallen),controlegetal1),
        f"{grootste_getal_in_lijst(getallen)} / {controlegetal2}": gedeeld_door_tweede_controle_getal_1(grootste_getal_in_lijst(getallen),controlegetal2),
        "Aantal unieke elementen": aantal_elementen(unieke_getallen_selecteren(getallen)),
        f"Het verschil tussen {aantal_elementen(unieke_getallen_selecteren(getallen))} & {controlegetal1}": verschil_tussen_elementen(aantal_elementen(unieke_getallen_selecteren(getallen)) , controlegetal1),
        "Gesorteerde lijst getallen": gesorteerde_lijst(getallen),
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst(unieke_getallen_selecteren(getallen)),
        "Telling van elementen": elementen_tellen(getallen),
        f"Deelbaar door {controlegetal1} (op volgorde)": getallen_deelbaar_door_acht(unieke_getallen_selecteren(getallen)),
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar_door_tweede_controle_getal(unieke_getallen_selecteren(getallen)),
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komt_voor_in_bepaalde_lijst(getallen),
        f"{controlegetal1} komt voor op positie(s)": vind_posities_van_eerste_getal(getallen),
        "Standaardafwijking": bereken_standaardafwijking(gemiddelde_berekenen(opgetelde_sommen_van_lijst(getallen),gemmideld_aantal(getallen)) , getallen , gemmideld_aantal(getallen)),
        "Geshufflede lijst": shuffle_de_lijst(getallen),
        "Willekeurige getal uit de lijst": random_getal_uit_lijst(getallen , gemmideld_aantal(getallen)),
        f"Het verschil tussen {random_getal_uit_lijst(getallen,gemmideld_aantal(getallen))} & {controlegetal2}": verschil_tussen_getallen(random_getal_uit_lijst(getallen,gemmideld_aantal(getallen))),

    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")