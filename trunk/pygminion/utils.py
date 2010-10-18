import string

def cmpMoney(a, b):
    try:
        a = a.lower()
        b = b.lower()
        return cmp(int(a), int(b))
    except ValueError:
        # Something has a potion in the cost...
        
        a_coins = sum([int(c) for c in a if c in string.digits])
        b_coins = sum([int(c) for c in b if c in string.digits])
        a_potions = sum([1 for c in a if c == 'p'])
        b_potions = sum([1 for c in b if c == 'p'])
        
        # Equal?
        if a_coins == b_coins and a_potions == b_potions: return 0
        
        elif a_coins < b_coins or a_potions < b_potions: return -1
        
        else: return 1

def addMoney(a, b):
    a = a.lower()
    b = b.lower()
    
    a_coins = sum([int(c) for c in a if c in string.digits])
    b_coins = sum([int(c) for c in b if c in string.digits])
    a_potions = sum([1 for c in a if c == 'p'])
    b_potions = sum([1 for c in b if c == 'p'])
    
    return str(a_coins + b_coins) + "p"*(a_potions + b_potions)
        
