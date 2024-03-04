class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s) : 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0 
                continue
            dp[i] = dp[i + 1]
            if (i + 1 < len(s) and int(s[i:i+2]) <= 26):
                dp[i] += dp[i + 2]
        
        return dp[0]

        # recursion
        
        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0
            
            n_ways = dfs(i + 1)
            if (i + 1 < len(s) and int(s[i:i+2]) <= 26):
                n_ways += dfs(i + 2)
            
            dp[i] = n_ways
            return n_ways
        
        return dfs(0)

        