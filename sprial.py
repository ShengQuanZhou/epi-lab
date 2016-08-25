#!/usr/bin/anaconda3/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 22:52:58 2016

Spiral Ordering of a 2D array

@author: quan
"""

#A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
A = [[1,2,3],[4,5,6],[7,8,9]]

N = len(A)
N2 = N*N

i=0
j=0

index=0
direction = 'E'
upper = N
lower = 0

while index < N2:
    print(A[i][j])
    if direction == 'E' and j < upper:
        j += 1
        if j == upper-1: 
            direction = 'S'
    elif direction == 'S' and i < upper:
        i += 1
        if i == upper-1: 
            direction = 'W'
            upper -= 1
    elif direction == 'W' and j >= lower:
        j -= 1
        if j == lower: 
            direction = 'N'
            lower += 1
    elif direction == 'N' and i >= lower:
        i -= 1
        if i == lower: direction = 'E'
        
    index += 1
