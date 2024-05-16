
# import pywhatkit


# phone_number = input("telefoon nummer ")
# message = input("message? ")
# time_hours = int(input("uur? "))
# time_minutes = int(input("minuten "))

# pywhatkit.sendwhatmsg(phone_number,message,time_hours,time_minutes)

import pywhatkit

# Eenmalig invoeren van het telefoonnummer
phone_number = input("Telefoonnummer: ")

while True:
    message = input("Bericht (of typ 'q' om te stoppen): ")
    
    if message.lower() == 'q':
        break

    time_hours = int(input("Uur: "))
    time_minutes = int(input("Minuten: "))

    pywhatkit.sendwhatmsg(phone_number, message, time_hours, time_minutes)