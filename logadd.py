__author__ = 'Franklou'
# -*- coding: utf-8 -*-


import numpy as np
## Function for logarithm addition
## A = log(a); B = log(b);
## Y = log(a+b)--> A + log(1+e^(B-A))


def logadd(x, y):
    cc = x + np.log(1 + np.exp((y - x)))
    return cc
