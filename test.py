woord = "blaat"
woord1 = "test"

max_length = 20

lenwhitespaces = max_length - len(woord)
x = 0
ws = ""

while x <= lenwhitespaces:
    ws += " "
    x +=1

print(f"  {woord}{ws}{woord1}")
