from string import ascii_lowercase
import random
from colorama import Fore
random_woorden = [
    "appel",
    "banaan",
    "citroen",
    "druif",
    "elephant",
    "fiets",
    "giraffe",
    "hond",
    "ijsbeer",
    "jacht",
    "kameleon",
    "leeuw",
    "mango",
    "neushoorn",
    "octopus",
    "papegaai",
    "quiche",
    "roos",
    "schildpad",
    "tijger",
    "uil",
    "vliegtuig",
    "walvis",
    "xylofoon",
    "yoga",
    "zebra"
]

lijst_met_foute_letters = []
pogingen = 10
te_raden = random.choice(random_woorden)
geraden = list("_" * len(te_raden))
# vraag gebruiker om letter

def get_letter() -> str:
    while True:
        letter = input('vul een letter in: ')
        if letter not in ascii_lowercase:
            print('je moet wel een kleine letter invullen') 
        elif len(letter) != 1:
            print('voer 1 letter in')
        else:
            
            return letter

while pogingen >0:
    ingevulde_letter = get_letter()
    print(ingevulde_letter)

    

    

    ingevulde_letter = ingevulde_letter
    gerade_list = list(geraden)

    # check if letter is in word
    if ingevulde_letter in te_raden:
        print('zit erin')
    # letter plaatsen
        for pos , letter in enumerate(te_raden):
            if letter == ingevulde_letter:
                geraden[pos] = letter
        
        print(f"je hebt al geraden: {''.join(geraden)}") 
    elif ingevulde_letter not in te_raden:
        lijst_met_foute_letters.append(ingevulde_letter)
        print(f'deze letter staat niet in het woord')
        print(f'de foute letters: {lijst_met_foute_letters}')
    pogingen -=1
    print(f'je hebt nog {pogingen} pogingen over')
    if pogingen == 0:
        print(f'Game over :( het woord was {te_raden}')
    #melde foute letter bijhouden hoevaak je het fout heb gedaan