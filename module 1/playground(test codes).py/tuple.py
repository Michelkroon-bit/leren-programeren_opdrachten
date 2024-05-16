def bereken_hoog_btw_inc(bedrag_ex):
    BTW=1.21
    bedrag_incl = round(bedrag_ex * BTW, 2)
    return bedrag_incl
# testjes
# print(bereken_hoog_btw_inc(100))
# print(bereken_hoog_btw_inc(50))
bonnetje = (3.15 , 2.45 , 7.2)  
    
#print de bedragen met excl.btw en incl btw

for bedrag in bonnetje:
    bedrag_in =bereken_hoog_btw_inc(bedrag)
    print(f"excl.: €-{bedrag} incl: -{bedrag_in})