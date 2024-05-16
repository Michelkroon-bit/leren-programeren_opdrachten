from test_lib import *
from math import floor , ceil


AANTAL_CENTEN = 5
getal1 = 18.67


def afronden_met_stuivers(getal1:float,):
    uitkomst = (round(getal1 *100 / 5) * 5 / 100)
    return '{:.2f}' .format(round(uitkomst, 2))



expected ='{:.2f}' .format(round(18.65, 2))
calculated = afronden_met_stuivers(getal1)


test('afronding', expected , calculated)
print(afronden_met_stuivers(getal1))
report()
