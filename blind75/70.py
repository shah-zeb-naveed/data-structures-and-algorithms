class Solution:
    def climbStairs(self, n: int) -> int:
         
        # cache = {0:1,1:1} # init base case
        # def dfs(n):
        #     #if n == 0 or n == 1: return 1
        #     if n in cache: return cache[n]
        #     cache[n] = dfs(n - 1) + dfs(n - 2)
        #     return cache[n]

        # return dfs(n)

        # dp
        # equation
        # dp[i] = dp[i - 1] + dp[i - 2]
        # dp[0] = 1
        # dp[1] = 1
        # dp[2] = dp[1] + dp[0]= 2
        # dp[3] = dp[2] + dp[1] = 2 + 1 = 3
        
        #dp = [0] * (n + 1)
        #dp[0], dp[1] = 1, 1
        prev, cur = 1, 1
        for i in range(2, n + 1):
            new = prev + cur
            prev = cur
            cur = new
        return cur

         