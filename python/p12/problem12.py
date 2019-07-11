#!/usr/bin/python

# Calculate nth trianble number
def triangleNumber(n):
    a = 1
    tri = 0
    
    if n < 1:
        return 0

    while a <= n:
        tri += a
        a += 1
    
    return tri

def divisorNumber(n):
    num = 0
    i = 1

    while i <= n:
        if n%i == 0: 
            num += 1
        i += 1
    
    return num

n = 1

while divisorNumber(triangleNumber(n)) <=500:
    n += 1
    if n % 1000 == 0: print "*"

print n, trianbleNumber(n), divisorNumber(triangleNumber(n))
