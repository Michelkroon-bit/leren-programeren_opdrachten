import time
import random
from M3_D4_O4_De_code_van_een_ander_function import *
import termcolor
from colorama import Fore


User_stats = {'hp': 10, 'atk': 0, 'dmg': 0}
Monster_stats = {'monster_hp_fase1': 7, 'monster_hp_fase2': 9, 'monster_hp_fase3': 17}
maxhp = 10
hp = 10
atk = 0
dmg = 0
max_boss_hp = 50
sleepcount = 0
attackcount = 0

print(input(Fore.YELLOW+"Druk op ENTER om te starten"))
print(Fore.GREEN+"Dit is een tekst adventure game. Het doel van het spel is om in 10 dagen een character te maken sterk genoeg om de baas te verslaan!")
time.sleep(2)

# Character Setup
while True:
    name = input("Wat is de naam van je character? ")
    freestat = input("Je krijgt een bonus +3 voor een stat naar keuze welke kies je? (hp | atk) ")
    if freestat.lower() == "hp":
        maxhp += 3 
        print("Je hebt hp gekozen")
        break
    elif freestat.lower() == "atk":
        atk += 3
        print("Je hebt atk gekozen")
        break

hp = maxhp
print(f"hp: {hp} atk: {atk}")

def fight_day(monster_hp, monster_attack_func, hp_gain, atk_gain, monster_desc):
    global hp, atk, dmg, sleepcount, attackcount

    while True:
        action = input("Wat wil je vandaag doen? (Vechten, Slapen) ").lower()

        if action == "vechten":
            time.sleep(2)
            print(monster_desc)
            time.sleep(2)
            print(f"Het monster heeft {monster_hp} hp")
            time.sleep(2)
            
            while hp > 0:
                damage = monster_attack_func()
                print(f"Je wordt geraakt voor {damage}")
                hp -= damage
                print(f"hp: {hp} atk: {atk}")

                if hp <= 0:
                    print(Fore.RED + "Je bent dood GAME OVER!!!")
                    exit()

                action = input("Wat wil je doen (Aanvallen, Rennen) ").lower()

                if action == "aanvallen":
                    damage_u = attack_list_u()
                    print(f"Je valt aan voor {damage_u + atk}")
                    dmg += damage_u + atk

                    if dmg >= monster_hp:
                        print("Je hebt Gewonnen !!")
                        dmg = 0
                        attackcount += 1
                        random_stat = stat_list()
                        if random_stat.lower() == "hp":
                            maxhp += hp_gain
                            print("Je hebt extra hp gekregen")
                        elif random_stat.lower() == "atk":
                            atk += atk_gain
                            print("Je hebt extra atk gekregen")
                        return
                    
                elif action == "rennen":
                    print("Je bent weggerend")
                    time.sleep(2)
                    print("Einde dag")
                    return

        elif action == "slapen":
            hp = maxhp
            sleepcount += 1
            print(f"hp: {hp} atk: {atk}")
            print("Je hebt geslapen, je HP is weer naar zijn maximum")
            return

def boss_fight():
    global hp, atk, dmg

    while True:
        action = input("Wat wil je vandaag doen? (Vechten) ").lower()
        if action == "vechten":
            time.sleep(2)
            boss = Boss_list()
            print(f"je ziet de Boss {boss}")
            time.sleep(2) 

            print(f"De Boss heeft {max_boss_hp} hp en kan de SKILL {boss.lower()}ball gebruiken")

            while hp > 0:
                random_skill = skill_list_BOSS()

                if random_skill == {"ATCK"}:
                    damage = attack_list_BOSS()
                else:
                    damage = attack_skill_list_BOSS()
                    print(f"Je wordt geraakt door een {boss.lower()}ball voor {damage}")

                hp -= damage
                print(f"hp: {hp} atk: {atk}")

                if hp <= 0:
                    print("Je bent dood GAME OVER!!!")
                    print(f"De boss had nog {max_boss_hp - dmg} HP")
                    exit()

                action = input("Wat wil je doen (Aanvallen, Rennen) ").lower()

                if action == "aanvallen":
                    damage_u = attack_list_u()
                    print(f"Je valt aan voor {damage_u + atk}")
                    dmg += damage_u + atk

                    if dmg >= max_boss_hp:
                        print("Je hebt Gewonnen !!")
                        print(f"Je hebt de Boss verslagen met als max stats {maxhp} hp en {atk} atk")
                        print(f"je heb {sleepcount} keer geslapen en {attackcount} keer gevochten")
                        exit()
                    
                elif action == "rennen":
                    print("Je bent weggerend van de boss")
                    time.sleep(2)
                    print("Game Over")
                    exit()

for day in range(1, 11):
    print(f"Dag {day}")
    if day < 4:
        fight_day(random.randint(7, 12), attack_list, 3, 3, monster_list(name))
    elif day < 7:
        fight_day(random.randint(7, 12), attack_list2, 5, 5, monster_list_2(name))
    else:
        fight_day(random.randint(7, 12), attack_list3, 7, 7, monster_list_3(name))

print("Boss fight")
boss_fight()
