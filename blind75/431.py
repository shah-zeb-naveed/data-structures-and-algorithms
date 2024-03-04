from typing import (
    List,
)
from lintcode import (
    UndirectedGraphNode,
)

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        
        # dfs
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            connected.append(node.label)
 
            for ne in node.neighbors:
                dfs(ne)
            
        visited = set()
        res = []
        # O(N)
        for node in nodes:
            connected = []
            if node not in visited: dfs(node)
            if connected: res.append(list(connected))

        # O(k = # of connected components)
        for c in res:
            # O(m log m)
            c.sort()

        return res

        # union find
        from collections import defaultdict
        edges = set()
        for node in nodes:
            for ne in node.neighbors:
                if (ne.label, node.label) not in edges:
                    edges.add((node.label, ne.label))
        
        pars = [i for i in range(len(nodes) + 1)]# * len(nodes)
        rank = [1] * (len(nodes) + 1)
        def find(node):
            res = node
            while res != pars[res]:
                pars[res] = pars[pars[res]]
                res = pars[res]
            
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return 0

            if rank[p1] > rank[p2]:
                pars[p2] = p1
                rank[p1] += rank[p2]
            else:
                pars[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = len(nodes)
        #print(edges)
        for n1, n2 in edges:
            #print(n1, n2)
            res -= union(n1, n2)
    
        print(res)
        return res











