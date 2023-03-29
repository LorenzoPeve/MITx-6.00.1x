

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1

    if exp == 1:
        return base
    
    return base * recurPower(base, exp -1)
    

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1


    total = base
    while exp > 1:
        total *= base
        exp -= 1
    return total

print(iterPower(2, 4))


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    val = min(a, b)
    while val > 1:
        if a % val == 0 and b % val == 0:
            break
        val -= 1
    return val

print(gcdIter(9, 12))

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print(gcdRecur(119, 112))