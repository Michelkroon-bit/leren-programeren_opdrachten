begin = 50
som=(f"{begin}")
optel=begin+1
uitkomst = begin
while uitkomst <= 1000:
    som = (f"{som}+{optel}")
    uitkomst = uitkomst + optel
    print(f"{som}={uitkomst}")
    optel += 1
#AF
