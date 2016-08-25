#!/usr/bin/anaconda3/bin/python

"""
Created on Tue Aug 24 22:55:00 2016

Traverse a binary tree in the order of depth

@author: quan
"""

from binary_tree import Node
from binary_tree import Tree

from collections import deque

def BinaryTreeDepthOrder(tree):
    result = []
    curr = tree.get()
    processing_nodes = deque([curr])
    number_of_processing_nodes = len(processing_nodes)

    while processing_nodes:
        curr = processing_nodes.popleft()
        number_of_processing_nodes -= 1

        if curr is not None:
            result.append(curr.v)
            processing_nodes.append(curr.l)
            processing_nodes.append(curr.r)

        if not number_of_processing_nodes:
            number_of_processing_nodes = len(processing_nodes)
            
    return result 

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

    print(BinaryTreeDepthOrder(tree))


