#!/usr/bin/anaconda3/bin/python

"""
Created on Tue Aug 27 22:38:00 2016

Find the k'th largest elements in a BST

@author: quan
"""

from binary_tree import Node
from binary_tree import Tree

def BstFindKLargest(k, tree):
    k_largest = []
    BstFindKLargestHelper(tree.get(), k, k_largest)
    return k_largest

def BstFindKLargestHelper(root, k, k_largest):
    if root and len(k_largest)<k:
        BstFindKLargestHelper(root.r, k, k_largest)
        if len(k_largest)<k:
            k_largest.append(root.v)
            BstFindKLargestHelper(root.l, k, k_largest)

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
    print(BstFindKLargest(5, tree))
