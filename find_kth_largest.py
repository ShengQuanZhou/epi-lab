#!/usr/bin/anaconda3/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:18 2016

Find the k'th largest element
Assume all elements are distinct

@author: quan

"""

import random
import math
from pivot import DutchFlagPartition

def FindKthLargest(k, A):
    n = len(A)
    A_partial = A[0:n]
    while n>0:
        # take random pivot; could be middle point also
        pivot_index = math.floor(n * random.random())
        new_pivot_index = DutchFlagPartition(pivot_index, A_partial)
        if new_pivot_index == n-k:
            return A_partial[new_pivot_index]
        elif new_pivot_index > n-k:
            A_partial = A_partial[0:new_pivot_index]
            k -= (n-new_pivot_index)
            n -= (n-new_pivot_index)
        else:
            A_partial = A_partial[new_pivot_index+1:n]
            n -= (new_pivot_index + 1)

if __name__ == "__main__":
    A = [1, 9, 2, 5, 3, 7, 15, 4, 12, 6, 8, 11]
    print(FindKthLargest(3, A))

