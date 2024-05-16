def get_value(data: str, separator: str, position: int) -> str:

  
  splitted_strings = data.split(separator) # string splits itself into collection of strings
  print(splitted_strings)
  print(len(splitted_strings))
  if 0 <= position< len(splitted_strings):
    value = splitted_strings[position] # read value at position of split_values
  else:
    value = None
  
  print(value) # prints: Bram:6
  return value


toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position= 6 # position of Bram, first position starts with 0

var1=get_value( toets_data , separator , position )
print(var1)
var2 = get_value('appel ,banaan, aarbij , peer' , ',' , 1 )
print(var2)