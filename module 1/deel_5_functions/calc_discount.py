from test_lib import *
from math import*
from test_lib import test , report


month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10


def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands:
        discount = price * MONTH_DISCOUNT_PERC /100
    else:
        discount = 0
    return round(discount, 2)

expected = 10.00
calculate = calc_discount (100 , 'Vespa' , month_discount_brands)
test('value', expected , calculate)

expected = 20.00
calculate = calc_discount (200 , 'Yamama' , month_discount_brands)
test('Yamama', expected , calculate)


report()




# Maak deze function calc_discount verder af
# De function moet de korting berekenen en opleveren, niet de gekorte prijs.
# Korting wordt berekend als: de prijs maal kortingspercentage gedeeld door honderd. Maar alleen als het merk (brand) voorkomt in de lijst met discount merken (month_discount_brands). Anders wordt de korting nul.
# Rond de bedragen af op 2 decimalen.
# Maak de function werkend.
# Verander de parameters niet.
# Test op 5 verschillende testgevallen en uitzonderingen. Zorg dat de function fool-proof is. LET OP: geen print() of input() in de function. Gebruik de test_lib.