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

def digit(n:int):
    '''
    数値nの桁数を整数で返す。負の場合は絶対値の桁数。
    '''
    n = math.abs(n)
    if n == 0: return 0
    return int(math.log10(n))+1
