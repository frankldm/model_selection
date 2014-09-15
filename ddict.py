__author__ = 'Franklou'
# -*- coding: utf-8 -*-
# It is to count the number of figure appear in the True table
# A = [1,4,1,4,6,5,5,5,4,2,3] // B = [1, 3, 4, 5]
# ddict(A, B) = [[0, 2] [10] [1, 3, 8] [5, 6, 7]]
import numpy as np


def ddict(src, truet=None):
    """\
    Example using defaultdict to group value indexes with optional mask

    """
    ddl = defaultdict(list)

    for idx, val in enumerate(src):
        if truet is not None and val not in truet:
            continue

        ddl[val].append(idx)
    tmp = np.array(ddl.values())
    return tmp
