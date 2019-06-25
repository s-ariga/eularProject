import math

def is_prime(n : int):
    '''
    素数かどうか判定
    
    parameters
    ---------------
    n : int
    判定する整数(負の数でもOK Falseだけど)

    returns
    ---------------
    bool

    '''
    if type(n) is not int: return False 
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    for k in range(3, int(math.sqrt(n))+1, 2):
        if n % k == 0:
            return False
    return True
