__author__ = 'Franklou'
# -*- coding: utf-8 -*-
import numpy as np
import sys


sys.path.append('/Users/Franklou/Dropbox/TUe/Traineeship/Code/Py')
q = np.loadtxt("q.txt", dtype='f8')
#q = np.matrix([[10, 12, 34, 33], [10, 11, 12, 0], [333, 332, 0, 0], [444,0, 0,  0]])
m = np.shape(q)
n = m[0]
bb = np.zeros(shape=(n, n))
b = -q
i = 2
for ii in range(1, n-i+2):
    dd = b[0:i-1, ii]
    cc = np.diag(b[0:i-1, ii+i-1:-1:ii+1])
    ccc = np.flipud(cc)
    if (dd+ccc) < b[i, ii]:
        bb[i-1, ii-1] = 0
    else:
        bb[i-1, ii-1] = 1


if bb[1, 1] > 0:
    bb[0, 0] = 1
    bb[0, 1] = 1

for nn in range(2, n):
    if bb[1, nn-1] > 0:
        bb[0, nn-1] = 1
        bb[0, nn] = 1

for n in range(3, n+1):
    for iii in range(1, n):
        if (bb[n-2, iii-1]+bb[n-2, iii]) > 1:
            bb[n-1, iii-1] = 1
