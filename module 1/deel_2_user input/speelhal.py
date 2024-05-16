aantal_personen = int(input('hoeveel personen zijn er '))
vip_vr_gameset=int(input('hoeveel minuten vr wil je '))



PRIJS_PER_PERSOON=7.45 #CENT
VIP_VR_GAMESET=0.37#CENT
VR_PRIJS_PER_MINUTEN=5



uitkomst = PRIJS_PER_PERSOON * aantal_personen*100
print (f'de prijs per persoon is',uitkomst,'cent')


vr_vip1 = VIP_VR_GAMESET /VR_PRIJS_PER_MINUTEN
vr_vip2 = vr_vip1 * vip_vr_gameset *100

uitkomst_vip2 = (vr_vip1 * aantal_personen)*100
totaal = int(round(vr_vip1 , 2))
print ('de prijs voor de vip vr gameseat is',uitkomst_vip2,'cent')
totaal = uitkomst + uitkomst_vip2/100


print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {aantal_personen} personen voor {vip_vr_gameset} minuten VR kost je maar {totaal}')

#todo:printjes omrekenen in euros