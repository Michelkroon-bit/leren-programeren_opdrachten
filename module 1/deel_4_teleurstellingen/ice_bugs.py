def convertToEuroText(amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25# heb de comma in een punt veranderd
MEDIUM_PRICE = 2.10# heb de comma in een punt veranderd

amount = float(input('Hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(SMALL_PRICE)))) # float toegevoegd anders was het een string input
amount_1 = float(input('En hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(MEDIUM_PRICE)))) # float toegevoegd en variable naam  veranderd
totalPrice = amount * SMALL_PRICE + amount_1 * MEDIUM_PRICE # int value veranderd naar float value

print('Dat is dan {} totaal'.format(convertToEuroText(totalPrice)))
