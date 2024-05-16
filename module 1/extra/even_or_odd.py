
def even_or_odd(nummer):
     if nummer % 2 == 0:
         return "Even"
     else:
         return "Odd"
nummer = int(input('vul een nummer in: '))
antwoord = even_or_odd(nummer)
print(antwoord)