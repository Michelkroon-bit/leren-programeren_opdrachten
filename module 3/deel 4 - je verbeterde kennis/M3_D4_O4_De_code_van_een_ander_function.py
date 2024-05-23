import time
import random
OPTION_A = ('a','A')
OPTION_B = ('B','b')

def monster_list(naam: str) -> str:
    Monsters = ("Goblin", "Slijm",)
    random_monster = random.choice(Monsters)
    return f"{naam} ziet een {random_monster}"

def monster_list_2(naam: str) -> str:
    Monsters2 = ("Golem", "Trol")
    random_monster2 = random.choice(Monsters2)
    return f"{naam} ziet een {random_monster2}"

def monster_list_3(naam: str) -> str:
    Monsters3 = ("Oni", "Spook")
    random_monster3 = random.choice(Monsters3)
    return f"{naam} ziet een {random_monster3}"

def Boss_list() -> str:
    Boss = ("Fire Storm", "Ice Storm")
    random_Boss = random.choice(Boss)
    return random_Boss

def stat_list() -> str:
    Stats = ("hp", "atk")
    random_stat = random.choice(Stats)
    return random_stat

def attack_list() -> int:
    damage = random.randint(1,3)
    return damage

def attack_list2() -> int:
    damage = random.randint(1,5)
    return damage

def attack_list3() -> int:
    damage = random.randint(3,7)
    return damage

def attack_list_BOSS() -> int:
    damage = random.randint(5,10)
    return damage

def attack_skill_list_BOSS() -> int:
    damage = random.randint(7,13)
    return damage

def skill_list_BOSS() -> str:
    skill = ("ATCK", "SKILL",)
    random_skill = random.choice(skill)

    return {random_skill}

def attack_list_u() -> int:
    damage_u = random.randint(1,7)
    return damage_u