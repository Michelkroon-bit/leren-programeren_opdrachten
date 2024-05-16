adventurerGear = [{
    'name' : 'Lantaren',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
},{
    'name' : 'Lampenolie',
    'amount' : 2,
    'unit' : 'dl',
    'price' : {
        'amount' : 13,
        'type' : 'copper'
    }
},{
    'name' : 'Hengel',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
},{
    'name' : 'Schop',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
},{
    'name' : 'Tinderbox',
    'amount' : 3,
    'unit' : 'x',
    'price' : {
        'amount' : 8,
        'type' : 'copper'
    }
},{
    'name' : 'Rugzak',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 13,
        'type' : 'silver'
    }
},{
    'name' : 'Touw',
    'amount' : 3,
    'unit' : 'meter',
    'price' : {
        'amount' : 14,
        'type' : 'silver'
    }
},{
    'name' : 'Fakkel',
    'amount' : 2,
    'unit' : 'x',
    'price' : {
        'amount' : 12,
        'type' : 'silver'
    }
},{
    'name' : 'Waterzak',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 11,
        'type' : 'silver'
    }
}]

testarg_items_test1 = [{
    'name' : 'Kaars',
    'amount' : 3,
    'unit' : 'x',
    'price' : {
        'amount' : 4,
        'type' : 'copper'
    }
}]


# def getItemsAsText(items:list) -> str:
#     for x in items:
#         return(f"{x['amount']}{x['unit']} {x['name']} ")
            
            
# abc = getItemsAsText(testarg_items_test1)
# print(abc)

def getItemsValueInGold(items:list) -> float:
    for x in items: 
        return(f"{x['price']}")
    
abc = getItemsValueInGold(testarg_items_test1)
print(abc)