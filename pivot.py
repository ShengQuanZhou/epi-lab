#!/usr/bin/anaconda3/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 22:54 2016

Pivot an array A by an index i such that
all elements less than A[i] appears first,
followed by elements equal to the pivot,
followed by elements greater than the pivot.

@author: quan

"""

def DutchFlagPartition(pivot_index, A):
    """
    Keep the following invariants during partitioning:
    bottom group: A[0:smaller-1]
    middle group: A[smaller:equal-1]
    unclassified group: A[equal:larger]
    top group: A[larger+1:A.size()-1]
    """

    pivot = A[pivot_index]    

    smaller = 0
    equal = 0
    larger = len(A) - 1
    while equal <= larger:
        # A[equal] is the incoming unclassified element
        # -3 0 -1 5 1 1 ? ? 4 2
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1
    return equal-1

if __name__ == "__main__":
    A = [1, 9, 2, 5, 3, 3, 2, 7, 10, 4]
    new_pivot_index = DutchFlagPartition(1, A)
    print(new_pivot_index)
    print(A)
    A = [10, 7, 9, 6, 8]
    new_pivot_index = DutchFlagPartition(1, A)
    print(new_pivot_index)
    print(A)
