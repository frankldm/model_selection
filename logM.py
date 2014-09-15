__author__ = 'Franklou'
# -*- coding: utf-8 -*-

## B has been fliped
## It is a function: A =[1 2 3],B = [4,5,6]
## A*B'=1*4 + 2*5 +3*6 = 32,

## Now A and B is logarithm form
## A = log(a); B = log(b);
## y = A + log(1+e^(B-A));
import numpy as np


def logm(x, y):

        x = np.array(x)
        y = np.array(y)

        s = np.shape(x)
        s = np.array(s, dtype=float)
        c = np.zeros(s)
        for i in range(0, s):
            c[i] = x[i] + y[i]

        dd = np.zeros(shape=(1, s))
        dd[0] = c[0]

        for nn in range(1, s):
            dd = dd + np.log(1 + np.exp(c[nn] - dd))

        return dd
