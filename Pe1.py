__author__ = 'Franklou'
# -*- coding: utf-8 -*-
# import profile
import math
## It is a Pe probability function


def pe1(x, y):
    cc = math.gamma(x + 0.5) * math.gamma(y + 0.5) / (math.pi * math.gamma(x + y + 1))
    return cc

#profile.run('print pe(13,40);print')  ## function running time