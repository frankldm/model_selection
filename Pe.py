__author__ = 'Franklou'
# -*- coding: utf-8 -*-

## To calculate of Pe(a, b) = gamma(a+0.5)*gamma(b+0.5)/(pi*gamma(a+b+1))

import numpy as np
import scipy.special


def pe(x):
    x = np.array(x)

    n = np.shape(x)[0]

    h = np.zeros(shape=(1, n/2))

    for i in range(1, n, 2):
        #print i, x[i-1], x[i]
        d = scipy.special.gammaln(x[i-1]+0.5) + scipy.special.gammaln(x[i]+0.5) - (np.log(np.pi) + scipy.special.gammaln(x[i-1]+x[i]+1))
        a = i/2
        h[0][a] = d

    return np.sum(h)


