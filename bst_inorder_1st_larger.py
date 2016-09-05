#!/usr/bin/anaconda3/bin/python

"""
Created on Tue Aug 27 22:13:00 2016

Find the first key larger than a given value inorder traversal

@author: quan
"""

from binary_tree import Node
from binary_tree import Tree

def BstInorderFindFirstKeyLargerThan(v, tree):
    candidate = None
    curr = tree.get()
    while curr:
        if curr.v > v:
            candidate = curr.v
            curr = curr.l
        else:
            curr = curr.r
   
    return candidate

if __name__ == "__main__":
    tree = Tree()
    tree.add(19)
    tree.add(7)
    tree.add(43)
    tree.add(3)
    tree.add(11)
    tree.add(23)
    tree.add(47)
    tree.add(2)
    tree.add(5)
    tree.add(17)
    tree.add(37)
    tree.add(53)
    tree.add(13)
    tree.add(29)
    tree.add(41)
    tree.add(31)

    print(BstInorderFindFirstKeyLargerThan(23, tree))

