# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #float input that askes for a amount to pay then multyplies the answer with 100 then changes it to a int value
paid = int(float(input('Paid amount: ')) * 100) #float input that askes for the amount that was payed then he multyplies the answer by 100 then makes the answer a int value
change = paid - toPay # makes up the amound you have to give back in change 

coin500 = 0
coin200 = 0
coin100 = 0
coin50 = 0
coin20 = 0 
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0




if change > 0: # if statement that states that if change is greater then 0 coinvalue is 50
  coinValue = 500 # the coinvalue if change is greater then 0
  
  while change > 0 and coinValue > 0: # a while loop that states that if change is greater then 0 and coinvalue is greater rhen 0 then nr coins = change // coinvalue
    nrCoins = change // coinValue # varible nrcoins is change Floor division coinValue

    if nrCoins > 0: # if statement that states that if nrcoins is greater then 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #then print the macimal value of nr coins and coinvalue in cents
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #integer input that states how many cents you did return + str(coinValue) 
      change -= nrCoinsReturned * coinValue #variable change minus or equal to nrcoinsreturned times coinvalue 

# comment on code below:  if statement with multiple elif statements and a else statement which all have the variable coinvalue attached to it 
    if coinValue == 500:
      coin500 = nrCoinsReturned
      coinValue=200
      
    elif coinValue == 200:
      coin200 = nrCoinsReturned
      coinValue = 100
    
    elif coinValue == 100:
      coin100 = nrCoinsReturned
      coinValue = 50
      
    elif coinValue == 50:
      coin50 = nrCoinsReturned
      coinValue = 20
      
    elif coinValue == 20:
      coin20 = nrCoinsReturned
      coinValue = 10
      
    elif coinValue == 10:
      coin10 = nrCoinsReturned
      coinValue = 5
      
    elif coinValue == 5:
      coin5 = nrCoinsReturned
      coinValue = 2
      
    elif coinValue == 2:
      coin2 = nrCoinsReturned
      coinValue = 1
      
    else:
      coin1 = nrCoinsReturned
      coinValue = 0


if change > 0: # if statement that states that if change is greater then 0 it prints change not returned and else it prints done 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

print(f"{coin500}coins of 500 used")  
print(f"{coin200}coins of 200 used") 
print(f"{coin100}coins of 100 used") 
print(f"{coin50}coins of 50 used") 
print(f"{coin20}coins of 20 used") 
print(f"{coin10}coins of 10 used") 
print(f"{coin5}coins of 5 used") 
print(f"{coin2}coins of 2 used") 
print(f"{coin1}coins of 1 used") 
