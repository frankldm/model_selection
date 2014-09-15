__author__ = 'Franklou'
# -*- coding: utf-8 -*-

import numpy as np
import types

# np.random.rand: uniform distribution


def bool2(x, y):
    out = 1*(np.array(x > y, dtype=bool))
    return out


def andm(xx, yy):
    ## boolean function require same data type(int =! float)
    xx = xx.astype(int)
    yy = yy.astype(int)
    out = np.zeros(len(xx), dtype=int)
    for i in range(0, len(xx)):
        out[i] = 1*(xx[i] & yy[i])
    return out


t1 = 0.7
t2_1 = 0.6
t2_2 = 0.2

t3_1 = 0.2
t3_2 = 0.6
t3_3 = 0.2
t3_4 = 0.7

m = 1000   # number of object
n = 4   # number of feature

aa = np.random.rand(m, n)

b = bool2(aa[::, 1], t1)
c = np.dot(np.diag(b), aa[::, 2])

c = bool2(c, t2_1)
d = bool2(np.diag((np.ones(shape=(m, 1))-b)*aa[::, 2]), t2_2)

e1 = bool2(np.dot(np.diag(andm(b, c)), aa[::, 3]), t3_1)
e2 = bool2(np.dot(np.diag(b-c), aa[::, 3]), t3_2)
e3 = bool2(np.dot(np.diag(andm((np.ones(m)-b), d)), aa[::, 3]), t3_3)
e4 = bool2(np.dot(np.diag((np.ones(m)-b)-d), aa[::, 3]), t3_4)

dep = np.array([b, (c+d), (e1+e2+e3+e4)])
ind = bool2(np.random.rand(10, m), 0.5)
a = np.vstack([dep, ind]).T
## T: transposition, MxN

np.savetxt("a.txt", a, fmt='%i')
## fmt = '%i' type of data is int
