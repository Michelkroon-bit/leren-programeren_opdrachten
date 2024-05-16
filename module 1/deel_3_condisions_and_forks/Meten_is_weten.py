a= int(input('vul een getal in '))
b= int(input('vul een getal in '))

if a > b:
    max=a
    min=b
    print(f'a is het grootste getal:{max} ')
elif a < b:
    max=b
    min=a
    print(f'a is het kleinste getal{min}')
else: # a==b
    min = a
    max = a
    print('a en b zijn even groot') 
    
print(f'Het minimum is:gevolgd door de waarde van {min} Het maximum is:{max}')
    
    
    
        
 