__author__ = 'Franklou'

import numpy as np
import scipy.special

import math
import types
from collections import defaultdict

# c = np.zeros(shape=(2, 5))

# for i in range(0, 2):

#    for n in range(0, 5):
#
#           c[i][n] = n+1
#
#
# for ii in range(0,5):
#    c[0][ii] = ii*3
#    print c

# m = np.shape([2, 3])
# m = 3
n = [4, 4]
# n = np.array(n)
# print type(n)
# m = [3, 2]
# print type(m)
s = np.shape(n)
s = np.asarray(s, dtype=int)
#yy = np.zeros(s)
# print s,yy


#for i in range(0, s):
#    yy[i] = n[i]
#x = np.zeros(7)
#for i in range(0, 7):
#    x[i] = i
#    if x[i]


#print 1/float(3)

#print type(s), type(yy)

x = [[4], [1]]

y = [[1, 2, 3], [2, 3, 6]]
x = np.array(x)
y = np.array(y)

#m = np.shape(x)

#c = np.zeros(shape=(m[0], 1))


#for i in range(0, m[0]):
#    print i
#    c = c + x[i]
#    print c

#a = [8, 4, 0]
#d = [8, 4, 1]
#re = [0, 0, 0]
#a = np.array(a)
#d = np.array(d)
#print type(d)
#re = np.array(re)
#for i in range(0, 3):
#    d.(a[1, i])

#print re
#print (scipy.special.gammaln(1+0.5))
#print np.pi

def ddict_examp(src, msk=None):
    """\
    Example using defaultdict to group value indexes with optional mask

    """
    ddl = defaultdict(list)

    for idx, val in enumerate(src):
        if msk is not None and val not in msk:
            continue

        ddl[val].append(idx)

    tmp = np.array(ddl)
    return tmp

sss = np.ones(100)
#print sss
SRC = sss.tolist()
MSK = [1, 3, 5, 4, 10, 11, 12, 13, 0]
#print type(MSK)

d = np.zeros(len(MSK))
#print type(d), type(SRC), type(MSK)
for ii in range(0, len(MSK)):
    d[ii] = SRC.count(MSK[ii])

#print d
#print SRC.count(MSK[3])



ccc = [1, 2, 4], [1, 4, 5]
ccc = np.matrix(ccc)
ccc = ccc.tolist()
#print ccc, type(ccc)


#m = np.shape(np.matrix(MSK))
#print m[1]
#aa = np.zeros(m)
#for ii in range(0, m[1]):
#    aa[ii] = SRC.count(MSK[ii])

#print aa

#a = ddict_examp(SRC, MSK)

#bbb = np.matrix(SRC)
#a = np.array(a)
#print bbb
#print a
#print np.shape(bbb)

#a = np.array([1, 2, 3], [2, 3, 4])
#b = np.array([2, 3, 5], [3, 4, 4])
#print np.concatenate(([a], [b]))
#b = np.matrix(b)
#print a
#print b[0, 0]
def bool2(x, y):
    out = 1*(np.array(x > y, dtype=bool))
    return out

#print (bool2(np.random.rand(10, 4), 0.5))

#re = np.zeros(len(aaaa))
#print type(aaaa)
#bbbb = np.diag([1, 1, 1, 1, 1])
#print type(bbbb)
#for ii in range(0, len(bbbb)):

#    c = [i for i, x in enumerate(aaaa) if x == bbbb[ii]]
#
#    re[c] = re[c] + 1

#print re

#print type([a+b for a, b in zip(a, b)])

#print aa

#print zip(a, b), type(zip(a, b))

#print np.dot(bbbb, aaaa)

a = np.array([[0, 1, 4], [10, 2, 0], [11, 1, 2]])
x = np.array([[1, 2, 4], [1, 1, 1], [1, 1, 1]])

#print np.shape(a)
#print np.shape(x)

c = np.vstack([a, x])
#a = np.vstack((a, x[x[:, 0] < 3]))
a = np.matrix(a)
#print a
print np.flipud(a)
