# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>


"""
For a undirected graph with tree characteristics, we can choose any node as the root. The result
graph is then a rooted tree. Among all possible rooted trees, those with minimum height are
called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and
return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and
a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,
1] is the same as [1, 0] and thus will not appear together in edges.

https://leetcode.com/problems/minimum-height-trees/description/
"""


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]

        adj = [set() for _ in range(n)]
        for [i, j] in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                j = adj[leaf].pop()
                adj[j].remove(leaf)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves

        return leaves
