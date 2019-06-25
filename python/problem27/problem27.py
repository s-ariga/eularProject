def is_prime(n : int):
    '''
    return: 素数判定結果
    '''

    for i in range(2, n):
        if n <= 1:
            return False
        if n % i == 0:
            return False
    return True

def func(n: int, a: int, b: int):
    return n*n + a*n + b

max_n = 0
answer = 0

for a in range(-1000, 1001):
    print("Now calculating a = {0}, Max n = {1}".format(a, max_n))
    for b in range(-1000, 1001):
        n = 0
        while is_prime(func(n, a, b)):
            n += 1
    if n > max_n:
            max_n, max_a, max_b = n-1, a, b
print("n {0}, a {1}, b{2}".format(max_n, max_a, max_b))
print("answer = {0}".format(max_a * max_b))
