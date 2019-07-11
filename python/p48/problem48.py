#!/usr/bin/python

def lastDigits(a, n):
    return n%(10**a)

#print lastDigits(3, 3456789)

DIGIT = 12
MAX = 1000

answer = 0
for i in range(1,MAX+1):
    #print "i = ", i
    n = i
    for j in range(1,i):
        #print "j = ", j
        #print "n = ", n
        n = lastDigits(DIGIT, n*i)
    answer += n
    print "answer = ", answer

print lastDigits(DIGIT, answer)
