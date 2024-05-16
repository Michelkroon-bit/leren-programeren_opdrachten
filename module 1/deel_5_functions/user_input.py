def get_integer(string):
     uitkomst=int(string)
     return(uitkomst)
    
def get_float(string):
    flt_convert=float(string)
    return(flt_convert)


def get_string(string):
    str_convert=str(string)
    return(str_convert)

def get_letter(string):
    if len(string) == 1:
        if string.isalpha():
            print('deze letter staat in het alfabet')
            return(string.upper())
        else:
            print('dit caracter staat niet in het alfabet')
            return
    else:
        print("input is te lang")
        return
    
outputchar = get_letter(input('geef 1 letter '))
print(outputchar)
        