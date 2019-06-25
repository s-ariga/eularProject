#!/usr/bin/python3

import numpy as np


IMAX = 50
JMAX = 20
NUM = 13

a = np.loadtxt('array.txt', dtype='str')

c = np.empty((0,IMAX), int)
for b in a:
    c = np.append(c, np.array([int(i) for i in b]))
 
c = np.reshape(c, (JMAX, IMAX))

maxProduct = 0

# search for J axis
for j in range(0, JMAX-NUM+1):
    for i in range(0, IMAX):
        tmp = 1
        for k in range(0, NUM):
            tmp *= c[j+k][i]
        if tmp > maxProduct:
            maxProduct = tmp
            print([j, i, 0])

for j in range(0, JMAX):
    for i in range(0, IMAX-NUM+1):
        tmp = 1
        for k in range(0, NUM):
            tmp *= c[j][i+k]
        if tmp > maxProduct:
            maxProduct = tmp
            print([j, i, 0])

print(maxProduct)
#print(9*8*4*8*9*4*6*8*5*9*5*9*8) # 7, 29
#print(c[5,0], c[6,0])