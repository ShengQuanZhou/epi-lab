#!/usr/bin/anaconda3/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sep 5 11:54 2016

Given a dictionary D and two strings s and t,
write a program to determine if s produces t.
Define s to produce t if there exists a sequence
of strings from the dictionary P=<s0,s1,...,t>
such that the first string is s, the last string
is t, and adjacent strings have the same length
and differ in exactly one character. The sequence
is called a production sequence.

Assume that all charaters are lowercase alphabets.

If s does produce t, output the length of a 
shortest production sequence; otherwise, output -1.

@author: quan

"""

from collections import deque
from string import ascii_lowercase

def TransformString(D, s, t):
    """ Use BFS to find the least steps of transformation.
        See DirectedGraph.breadth_first_search for reference. """
    if s not in D or t not in D:
        return -1
    
    queue = deque([(s,0)])
    D[s] = True

    while queue:
        print(queue)
        if queue[0][0] == t:
            return queue[0][1]

        curr_list = list(queue[0][0]) # convert to list of characters
        curr_step = queue[0][1]
        size = len(curr_list)
        for i in range(size):
            for j in ascii_lowercase:
                curr_list[i] = j
                curr_string = ''.join(curr_list) # convert back to string
                if curr_string in D and not D[curr_string]:
                    D[curr_string] = True
                    queue.append((curr_string,curr_step+1))
            curr_list = list(queue[0][0]) # revert the change
        queue.popleft()
    
    return -1

if __name__ == "__main__":
    D = { "bat": None,
          "cot": None,
          "dog": None,
          "dag": None,
          "dot": None,
          "cat": None }
    s = "cat"
    t = "dog"
    print(TransformString(D, s, t))
