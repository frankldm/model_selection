__author__ = 'Franklou'
# -*- coding: utf-8 -*-


import sys
import numpy as np
import profile
import types


sys.path.append('/Users/Franklou/Dropbox/TUe/Traineeship/Code/Py')

from offt import offt

a = np.loadtxt("a.txt", dtype=int)
#a = np.array([[0, 1, 1], [0, 1, 0], [1, 1, 1]])
m = np.shape(a)
n = m[1]

q = np.zeros(shape=(n, n))

d =[]
for i in range(0, n):
    for ii in range(1, n+1):
        if (i+ii) > n:
            break
        else:
            d = a[::, ii-1:ii+i]
            q[i, ii-1] = offt(d)


np.savetxt("q.txt", q, fmt='%10.17f')
