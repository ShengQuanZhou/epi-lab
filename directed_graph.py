#!/usr/bin/anaconda3/bin/python

"""
Created on Tue Sep 4 23:24 2016

An implementation of directed graph 

@author: quan
"""

from collections import deque

class DirectedGraph:

    """ This is not necessarily the best
        implementation - for experiments only """

    def __init__(self, edges):
        self.edges = edges

    def get_successors(self, node):
        successors = []
        for edge in self.edges:
            if node == edge[0]:
                successors.append(edge[1])
        return successors

    def depth_first_search(self, node):
        """ The general idea is to keep moving
            nodes from the stack to the visited
            while adding the successors of the
            moved node to the stack, until the
            stack is empty."""
        visited = []
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.append(curr)
                successors = self.get_successors(curr)
                stack.extend(successors)
        return visited

    def breadth_first_search(self, node):
        """ The general idea is similar to
            BinaryTreDepthOrder, except that
            one needs to avoid cycles """
        visited = []
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            if curr not in visited:
                visited.append(curr)
                successors = self.get_successors(curr)
                for successor in successors:
                    if successor not in queue:
                        queue.append(successor)
        return visited

    def topological_sort(self, node):
        """ The general idea is to keep adding
            successors of nodes to the stack
            until a moved node has no successor.
            This idea was introduced to me by
            Manasvi Tickoo in summer 2016. """
        visited = []
        stack = [node]
        while stack:
            curr = stack[-1]
            successors = self.get_successors(curr)
            if not successors or set(successors) <= set(visited): 
                last = stack.pop()
                if last not in visited:
                    visited.append(last)
            else:
                stack.extend(successors)
        visited.reverse()
        return visited

if __name__ == "__main__":
    edges = [ ('a', 'b'),
              ('a', 'c'),
              ('a', 'd'),
              ('b', 'e'),
              ('c', 'f'),
              ('d', 'e'),
              ('e', 'f'),
              ('e', 'g') ]

    g = DirectedGraph(edges)
    print("Depth first search:")
    print(g.depth_first_search('a'))
    print(g.depth_first_search('e'))
    print(g.depth_first_search('d'))
    print("Topological sort:")
    print(g.topological_sort('a'))
    print(g.topological_sort('e'))
    print("Breadth first search:")
    print(g.breadth_first_search('a'))
    print(g.breadth_first_search('b'))



