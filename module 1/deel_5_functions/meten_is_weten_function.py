from test_lib import test, report
def getal_vergelijking(nr1:int , nr2:int)-> str:
    if nr1> nr2:
        return(f'Maximum: {nr1} en minimum: {nr2}')
    elif nr2 > nr1:
        return(f'Maximum: {nr2} en minimum: {nr1}')
    else:
        return('Beide getallen zijn even groot') 

nr1 = 20
nr2 = 10
expected = 'Maximum: 20 en minimum: 10'
functionreturn = getal_vergelijking(nr1, nr2)
test('Nr1 groter', expected, functionreturn)


nr1 = 10
nr2 = 20
expected = 'Maximum: 20 en minimum: 10'
functionreturn = getal_vergelijking(nr1, nr2)
test('Nr2 groter', expected, functionreturn)

nr1 = 20
nr2 = 20
expected = 'Beide getallen zijn even groot'
functionreturn = getal_vergelijking(nr1, nr2)
test('Nr1 en Nr2 zijn gelijk', expected, functionreturn)



nr1 = 15
nr2 = 350
expected = 'Maximum: 350 en minimum: 15'
functionreturn = getal_vergelijking(nr1, nr2)
test('extra test', expected, functionreturn)

report()