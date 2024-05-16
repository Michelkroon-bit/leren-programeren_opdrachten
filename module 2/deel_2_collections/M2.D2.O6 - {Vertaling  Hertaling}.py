from random import *

random_text = input("vul hier een zin in: ")
print("")
# text_split = random_text.split(" ")

vertaling = {"schild" : "batminton" ,"grot": "boom"}
# vertaling["schild"] = "batminton" 
# vertaling["grot"] = "boom"
vertaling["Draganthor"] = "vis" 
vertaling["schubben"] = "aap" 
vertaling["vlammenzee"] = "porch 911" 
vertaling["vurige"] = "tennisbal" 

for key in vertaling:
    random_text = random_text.replace(key,vertaling[key])

print(random_text)


# text 1: In het hart van de grot zagen ze Draganthor, met zijn glinsterende schubben en vurige ogen. De draak brulde en spuwde een vlammenzee die hen bedreigde, maar Rurik beschermde hen met een krachtig schild van magie.

#text 2: Diep in de donkere grot, omringd door glinsterende schubben, ontdekte avonturier Lara een eeuwenoud schild met onbekende runen. Plotseling doemde de Draginator op, een mythisch wezen met vurige ogen, en uit zijn muil brak een vlammenzee los. Met het magische schild trotseerde Lara de vurige aanval en onthulde zo de verborgen schatten van de grot.

#text 3: Op de rand van de betoverde vallei stond een eeuwenoude toren, bewoond door de wijze tovenaar Eldoran. Hij had een speciaal schild gecreëerd, versierd met drakenpatronen en doordrenkt met de kracht van de Vuurvogel. Toen de duistere schaduwen zich over de vallei verspreidden, ontketende Eldoran het schild, en het transformeerde de dreigende vlammenzee in een fonkelende regenboog van hoop, die de vallei voor altijd verlichtte.
























