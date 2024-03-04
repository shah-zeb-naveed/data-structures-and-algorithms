from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n: return True

        from collections import defaultdict
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
            
        
        # dfs
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False # detected
            
            # visit
            visited.add(node)
            # go deep
            for nei in adj[node]:
                # node = 2, prev = 0, nei = 0
                if nei == prev: continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visited)
