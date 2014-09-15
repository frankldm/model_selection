__author__ = 'Franklou'
# -*- coding: utf-8 -*-
import numpy as np
import sys

sys.path.append('/Users/Franklou/Dropbox/TUe/Traineeship/Code/Py')
from Pe import pe


def offt(x):
    ## m = size(A), m[0] row ; m[1] column
    x = np.matrix(x)
    m = np.shape(x)
    m = np.array(m)
    n = m[1]
    #print x, type(x), m
    #  row x column; m[0] --> row  m[1] --> column
    c = np.zeros(shape=m)
    c = np.matrix(c)
    #print type(c), type(x)#np.shape(c)
    for i in range(0, n):
        c[::, i] = (2**(n-i-1))*x[::, i]
    e = np.zeros(m)
    d = np.zeros(shape=(m[0], 1))
    #type of e is ndarray
    e = np.matrix(e)
    d = np.matrix(d)

    for ii in range(0, n):
            #print ii, np.shape(c[::, ii]), np.shape(d)
            d = np.sum([d, c[::, ii]], axis=0)
            # np.sum is function of summation of matrix, axis = 0 --> column by column
            e[::, ii] = d

    q = np. zeros(n)
    e = np.array(e)
    #The combination matrix = e
    ######
    # Build True table
    for iii in range(1, n+1):
        cc = np.linspace(2**iii-1, 0, 2**iii)
        d = 2**(n-iii)*cc
        # count & enumerate function requires list of data structure
        dd = d.tolist()
        ee = e[::, iii-1]
        eee = ee.tolist()

        re = np.zeros(len(dd))
        # re is to store the number of index appear in input
        for ii in range(0, len(eee)):
            # Here output of c is the location of index appear in true table array
            c = [i for i, x in enumerate(dd) if x == eee[ii]]
            # re[c] means to replace the position in true table with times it appears
            re[c] = re[c] + 1
        # q is to store logorithm value
        q[iii-1] = pe(re)

    return np.sum(q)