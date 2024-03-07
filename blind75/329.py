class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1] * COLS for _ in range(ROWS)]

        def dfs(i, j, prev):
            # base case
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or matrix[i][j] <= prev:
                return 0

            # cache case
            if dp[i][j] != -1: return dp[i][j]
            
            # recursion case
            ways = 0
            for nr, nc in [(1,0), (-1, 0),(0, 1),(0,-1)]:
                ways = max(dfs(i + nr, j + nc, matrix[i][j]), ways)            
            
            # save cache
            dp[i][j] = 1 + ways
            return dp[i][j]
        
        res = 1
        for i in range(ROWS):
            for j in range(COLS):
                ways = dfs(i, j, float('-inf'))
                res = max(res, ways)

        return res


        