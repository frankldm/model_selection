__author__ = 'Franklou'
# -*- coding: utf-8 -*-
# Calculate the number of terms for different features

import numpy as np
import math as math


def t1(x):
    if x == 1:
        dd = 1

    tt = np.zeros(x)
    #print tt
    for i in range(1, x):
        tt[i] = 1/float(i+1) * math.factorial(2*i) * math.factorial(x-1)/float(math.factorial(i)**3 * math.factorial(x-1-i))
        dd = np.sum(tt)+1

    return dd       
