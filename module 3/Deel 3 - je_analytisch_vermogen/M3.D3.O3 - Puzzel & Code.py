def reken_volgende_reeks_uit (reeks):
    volgende_reeks = ""
    count = 1
    for x in range(len(reeks)):
        if x + 1 < len(reeks) and reeks[x] == reeks[x + 1]:
            count +=1
        else:
            volgende_reeks += str(count) + reeks[x]
            
            count = 1
    
    return volgende_reeks        
    

# for i in range(9):  # bijvoorbeeld 10 keer om de eerste 10 termen te genereren
#     reeks = reken_volgende_reeks_uit(reeks)
#     print("Reek", i+2, ":",reeks)

while True:
    reeks = reken_volgende_reeks_uit(reeks)
    print(reeks)
    if '33' in reeks:
        break