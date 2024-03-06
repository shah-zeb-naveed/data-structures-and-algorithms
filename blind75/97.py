class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        # true dp: bottom up
        # O(N * M)
        # O(n*m) cache but no recursion stack so maybe more efficient
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # rows are s1
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j] == True:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1] == True:
                    dp[i][j] = True
                
        return dp[0][0]

        # memoization
        # O(M * N) because of possible keys and caching. Otherwise, 2 ^ (N + M)

        dp = {}

        def dfs(i, j): # k = i + j
            # base case
            if i == len(s1) and j == len(s2): return True # k points beyond s3
            
            # cache case
            if (i, j) in dp: return dp[(i, j)]

            # recursion
            possibility = False

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                possibility = True
                # this char can come from s1
                
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                possibility = True
                # this char can come from s2
            
            # save cache
            dp[(i, j)] = possibility
            return dp[(i, j)]

        
        return dfs(0, 0)