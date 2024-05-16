aantal_lijstjes=int(input("hoeveel lijstjes wilt u hebben: "))
lijstjes=[]
for lijst in range (1, aantal_lijstjes+1):
    lengte_lijstjes=int(input(f"hoe lang moet het lijstje {lijst} zijn?: "))
    lijstjes.append(list(range(lijst , lijst * lengte_lijstjes+1, lijst)))
print(lijstjes)
    

# print (f"aantal lijstjes: {aantal_lijstjes}")#for debugging
# print (f"lengte lijstjes: {lengte_lijstjes}")#for debugging 
  
# Eerst vraagt het programma om het aantal lijstjes dat getoond moet worden en vervolgens naar de lengte van ieder lijstje.

# Vervolgens toont het programma een aantal lijstjes met de gekozen lengte, waarbij de eerste bij 1 begint en stappen van 1 neemt, de tweede bij 2 begint en stappen van 2 neemt, de derde bij 3 begint en stappen van 3 neemt, enz, enz …

#lengte wordt bedoeld als in als je 4 invuld dat je print 4 cijfers lang moet zijn.

#GEBRUIK VOORBEELDEN!!!

#meer gebruik maken van voorbeelden!! 

