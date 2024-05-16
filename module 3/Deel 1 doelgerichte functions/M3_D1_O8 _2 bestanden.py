from M3_D1_O8_2_bestanden_bestand_1 import *

alle_namen = meer_namen_toevoegen()
for x in alle_namen:
    print(f"{x['namen']} die in {x['woonplaats']} woont is {x['leeftijd']} jaar oud")

