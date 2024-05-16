from test_lib import test, report
from math import floor, ceil, pow

#1
nr = 5.65499901
expected = 5.65
calculated = round(nr,2)
test('example', expected, calculated)

#2
nr = 13
expected = 13.0
calculated = float(nr) # use one function to calculate expected number
test('to-the-point',expected, calculated)

#3
nr = -45.372
expected = 45.372
calculated = abs(nr) # use one function to calculate expected number
test('optimistic', expected, calculated)

#4
nr = -45.372
expected = -45.4
calculated = round(nr, 1) # use one function to calculate expected number
test('approximately', expected, calculated)

#5
nr = 45.372
expected = -45.372
calculated = -abs(nr) # use one function to calculate expected number
test('pessimistic', expected, calculated)

#6
nr = -2.3
expected = floor(-3)
calculated = floor(nr) # use one function to calculate expected number
test('depressed', expected, calculated)

#7
nr = -7.25
expected = int(-7)
calculated = int(nr) # use one function to calculate expected number
test('pointless', expected, calculated)

#8
nr = 15.11
expected = 16
calculated = ceil(nr) # use one function to calculate expected number
test('sky-is-the-limit', expected, calculated)

report()



