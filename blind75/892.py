from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # fails case where [zy, zx]. not sure if test case is bad

        # Write your code here
        from collections import defaultdict
        
        adj = defaultdict(list)

        # O(N)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # invalid check
            smaller_length = min(len(w1), len(w2))
            # O(M)
            if len(w2) > len(w1) and w1[:smaller_length] == w2[:smaller_length]:
                return ''
            # O(M)
            # first difference
            j = 0
            while j < len(w1):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
                j += 1

        res = []
        path = {}

        def dfs(c):
            """
            topological sort. returns true if cycle detected
            """
            if c in path:
                return path[c] # return True if on active path

            path[c] = True # active path
            
            if c in adj: # remember this while using defaultdict
                for ne in adj[c]:
                    if dfs(ne): return True
            
            path[c] = False # backtrack but keep marked as visited
            res.append(c) # save after children

        for c in adj:
            if dfs(c): return ''

        res.reverse()
        return ''.join(res)

