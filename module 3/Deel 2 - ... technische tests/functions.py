import time
from termcolor import colored
from data import PEOPLE_PER_HORSE , PEOPLE_PER_TENT ,JOURNEY_IN_DAYS , COST_INN_HORSE_COPPER_PER_NIGHT , COST_INN_HUMAN_SILVER_PER_NIGHT , COST_FOOD_HUMAN_COPPER_PER_DAY , COST_FOOD_HORSE_COPPER_PER_DAY , CURRENCY_CONVERT_COPPER_SILVER , CURRENCY_CONVERT_PLATINUM_GOLD , CURRENCY_CONVERT_SILVER_GOLD, COST_TENT_GOLD_PER_WEEK , COST_HORSE_SILVER_PER_DAY 
from data import friends , adventurerGear
from math import ceil,floor

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / CURRENCY_CONVERT_COPPER_SILVER
    
    
def silver2gold(amount:int) -> float:
    return amount / CURRENCY_CONVERT_SILVER_GOLD

def copper2gold(gold:int) -> float:
    return silver2gold(copper2silver(gold))
    
    
    
def platinum2gold(amount:int) -> float:
    return amount * CURRENCY_CONVERT_PLATINUM_GOLD


def getPersonCashInGold(personCash:dict) -> float:
    return platinum2gold(personCash['platinum']) + copper2gold(personCash['copper']) + \
        silver2gold(personCash['silver'] ) + personCash['gold']
    
    
        
##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    dag_kosten_paard = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY)
    totale_kosten_persoon = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY) 
    #totaal = round(dag_kosten_paard * JOURNEY_IN_DAYS * horses + totale_kosten_persoon * JOURNEY_IN_DAYS * people , 2)
    totaal = round(((dag_kosten_paard * horses) + (totale_kosten_persoon * people)) * JOURNEY_IN_DAYS , 2)
    
    return totaal

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    resultaten = []
    
    for x in list:
        if key in x and x[key] == value:
            resultaten.append(x)
    return resultaten
        
def getAdventuringPeople(people:list) -> list:
    result = getFromListByKeyIs(people , 'adventuring' , True)
    
    return result

def getShareWithFriends(friends:list) -> list:
    result = getFromListByKeyIs(friends , 'shareWith' , True)
    
    return result

def getAdventuringFriends(friends:list) -> list:
    result = getFromListByKeyIs(friends , 'adventuring' , True)
   # result = getFromListByKeyIs('adventuring' ,'shareWith', getAdventuringPeople(friends))
    return result

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / PEOPLE_PER_HORSE)

def getNumberOfTentsNeeded(people:int) -> int:
    return ceil(people / PEOPLE_PER_TENT)

def getTotalRentalCost(horses:int, tents:int) -> float:
    kosten_tent = ceil(JOURNEY_IN_DAYS / 7) * COST_TENT_GOLD_PER_WEEK * tents
    kosten_paart = silver2gold(JOURNEY_IN_DAYS* COST_HORSE_SILVER_PER_DAY) * horses
    
    uitkomst = kosten_paart + kosten_tent
    return round(uitkomst , 1)

    

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    output_str = ''
    spullen = []
    for x in items: 
        zin = (f"{x['amount']}{x['unit']} {x['name']}")
        spullen.append(zin)
    counter = 0
    for x in spullen:
        if len(spullen) > 1:
            
            if counter == 0 :
                output_str += f'{x}'
            
            elif counter > 0 and counter != len(spullen) - 1:
                output_str += f', {x}' 
            else:
                output_str += f' & {x}' 
                
            counter +=1
        else:
            return x
    return output_str
    
    
    
def getItemsValueInGold(items:list) -> float:
    totale_uitkomst = 0.0
    index = 0
    for x in items:
        uitkomst_1 = x['amount'] * items[index]['price']['amount']
        
        if items[index]['price']['type'] == 'copper':
            totale_uitkomst += float(copper2gold(uitkomst_1))
            
        
        if items[index]['price']['type'] == 'silver':
            totale_uitkomst += float(silver2gold(uitkomst_1))
            
        
        if items[index]['price']['type'] == 'platinum':
            totale_uitkomst += float(platinum2gold(uitkomst_1))
            
        
        if items[index]['price']['type'] == 'gold':
            totale_uitkomst += uitkomst_1 #float(x['amount'] * items[0]['price']['amount'])
        index +=1  
    return totale_uitkomst

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totale_uitkomst = 0.0
    for person in people:
        totale_uitkomst = totale_uitkomst + getPersonCashInGold(person['cash'])
    return round(totale_uitkomst , 2)
        # return platinum2gold(single_person.get('platinum')) + copper2gold( single_person.get('copper')) + \
        #     silver2gold(single_person.get('silver')) + single_person.get('gold')

##################### O10 #####################


def getInterestingInvestors(investors:list) -> list:
    intresting_investor = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            intresting_investor.append(investor)
    return intresting_investor


def getAdventuringInvestors(investors:list) -> list:#aanpassen
    intresting_investors = getInterestingInvestors(investors) 
    adventuring_investors = []
    for investor in intresting_investors:
        if investor['adventuring'] == True:
            adventuring_investors.append(investor)
        
    return adventuring_investors


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    # intresting_investors = getInterestingInvestors(investors) 
    adventuring_investors = getAdventuringInvestors(getInterestingInvestors(investors))
    
    if len(adventuring_investors) <= 0:
        return 0.0
    else:
        return round(getTotalRentalCost(len(adventuring_investors), len(adventuring_investors)) + getJourneyFoodCostsInGold(len(adventuring_investors), len(adventuring_investors)) + getItemsValueInGold(gear) * len(adventuring_investors),2) 
        
    

##################### O11 #####################
def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    if leftoverGold <= 0:
        return 0
    
    else:
        return floor(leftoverGold /((people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT))+(horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT))))


def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    return round((copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT) + silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT)) * nightsInInn , 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    investor_cuts = []
    filterd_investor = getInterestingInvestors(investors)
    for investor in filterd_investor:
        uitkomst = profitGold /100 * investor['profitReturn']
        investor_cuts.append(round(uitkomst ,2))
    return investor_cuts

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float: 
    
    if profitGold <= 0:
        return 0.0 
    else:
        if fellowship == 0:
            return round((profitGold - sum(investorsCuts)),2)
        else:
            return round((profitGold - sum(investorsCuts)) / fellowship,2)

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold , investors)
    share_with_friends = getShareWithFriends(adventuringFriends)
    #goldCut = 0.0
    fellowship = share_with_friends + adventuringInvestors + [mainCharacter]
    # verdeel de uitkomsten
    for person in people:

        #main character 
        begin_bedrag = getPersonCashInGold(person['cash'])  
        if person == mainCharacter:
            eind_bedrag = begin_bedrag + getAdventurerCut(profitGold , investorsCuts , len(fellowship)) + (10 * len(share_with_friends))
        #Investors die meegaan
        elif person in adventuringInvestors:
            eind_bedrag = begin_bedrag + getAdventurerCut(profitGold , investorsCuts , len(fellowship)) + (profitGold / 100 * person['profitReturn'])
        #investors die niet meegaan
        elif person in interestingInvestors:
            eind_bedrag = begin_bedrag + (profitGold / 100 * person['profitReturn'])
        #Friends die meegaan
        elif person in share_with_friends:
            eind_bedrag = begin_bedrag +  getAdventurerCut(profitGold , investorsCuts , len(fellowship)) - 10
        else:
            eind_bedrag = begin_bedrag

        #code aanvullen
        earnings.append({
            'name'   : person['name'],
            'start'  : begin_bedrag,
            'end'    : eind_bedrag
        })

    return earnings


#check of de main character alleen het geld krijgt van de vrienden die meegegaan zijn
# je hebt de main character krijgt de adventurer cut en het schijnt zo te zijn dat zijn vrienden die meegingen hem allemaal 10 gold geven
# de vrienden die meegingen krijgen hun deel van adventurecut - 10 
# mensen die niet meegingen krijgen niks 
# de investors die meegingen krijgen adventures cut + hun profit return 
# de investors die niet meegingen maar wel profitreturn krijgen: hun profitreturn (persentage)
# alle investors die niet intresant zijn krijgen niks 
#
#

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()