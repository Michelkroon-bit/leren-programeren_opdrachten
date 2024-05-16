from studieadviestext import *

print(STUDIEDOKTER_TITEL)

print(AANTAL_WEKEN_VRAAG)
aantal_weken_vraag=(int(input()))

print(COMPETENTIE_STELLING_1)
print(OPTIES)
antwoord_1 = int(input())


print(COMPETENTIE_STELLING_2)
print(OPTIES)
antwoord_2=int(input())

print(COMPETENTIE_STELLING_3)
print(OPTIES)
antwoord_3 = int(input())

print(COMPETENTIE_STELLING_4)
print(OPTIES)
antwoord_4 = int(input())

print(COMPETENTIE_STELLING_5)
print(OPTIES)
antwoord_5 = int(input())

if aantal_weken_vraag >= 10:
    print(COMPETENTIE_STELLING_6)
    print(OPTIES)
    antwoord_6 = int(input())

if aantal_weken_vraag >= 10:
    print(COMPETENTIE_STELLING_7)
    print(OPTIES)
    antwoord_7 = int(input())

count0 = 0# telt hoevaak ieder antwoord gegeven wordt
count1 = 0# telt hoevaak ieder antwoord gegeven wordt
count2 = 0# telt hoevaak ieder antwoord gegeven wordt
count3 = 0# telt hoevaak ieder antwoord gegeven wordt
count4 = 0# telt hoevaak ieder antwoord gegeven wordt
  
total=0 #totaal
           
if aantal_weken_vraag >= 10:   
    antwoorden_lijst = [antwoord_1 , antwoord_2 , antwoord_3, antwoord_4 , antwoord_5]
    counthelft=3
else: 
    antwoorden_lijst = [antwoord_1 , antwoord_2 , antwoord_3, antwoord_4 , antwoord_5 , antwoord_6 , antwoord_7] 
    counthelft=4


# print("list length = " + str(len(antwoorden_lijst))) # for debugging

for x in antwoorden_lijst:
    total += x
    if x == 0:
       count0 += 1
    if x == 1:
       count1 += 1
    if x == 2:
       count2 += 1
       
       
       
       
       
       
       
    if x == 3:
       count3 += 1
    if x == 4:
       count4 += 1

gemiddelde= total // len(antwoorden_lijst)

# print(f'het totaal is: {total}')#totale score
# print(f' 1 en 0 kommen zovaak voor: {count0} + {count1}')# telt aantal 'punten' per antwoord
# print(gemiddelde)


print(COMPETENTIE_ADVIES_TITEL)

if (gemiddelde <= 2) or (count0 + count1 >= counthelft):
    print(COMPETENTIE_ADVIES_ZORGELIJK)
    print('Je advies is zorgelijk')

elif (gemiddelde == 3) or (count0 +count1 + count2 >= counthelft):
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
    print('Je advies is twijfelachtig')
    

else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
    print('Je advies is geruststellend')