# boodschappen=['melk' , 'eieren']

# boodschappen.append('brood')

# print (boodschappen)

# boodschappen= []
# bool_continue=True
# while bool_continue:
    
#     boodschap=input('wat wilt u toevoegen aan de lijst? ')
#     boodschappen.append(boodschap)
#     print('je item is toegevoegd')
#     verder_gaan=input('wilt u nog een item toevoegen ja/nee ')
#     if verder_gaan == 'nee':
# #         bool_continue=False


# print('dit is je boodschappen lijst')]
# for x in boodschappen:
#     print (x)

# section variables
bool_continue=True
list=[]



    # section main script
while bool_continue:
    list_item=input('vul een getal in ')  #ask a number
    list.append(list_item) # add to list
    print(list) # print list for debugging
    continue_list=input('wilt u nog een getal toevoegen ja/nee ')
    if continue_list == 'nee':
        bool_continue=False

print('dit is je lijst')
print(list)

for x in list:
    print(x)



    