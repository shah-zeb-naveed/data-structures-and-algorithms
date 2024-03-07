class Solution:
    def isMatch1(self, s: str, p: str) -> bool:
        # Initialize DP table with all False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Empty pattern matches empty string
        dp[len(s)][len(p)] = True

        # Fill DP table from bottom-up
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # Check if current characters match or pattern character is '.'
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j + 1] == '*':
                    # If there's a star, consider both cases: using and not using the star
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                else:
                    # If no star, characters must match and next characters must match
                    dp[i][j] = match and dp[i + 1][j + 1]

        return dp[0][0]


    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i, j):
            # base case
            # if both over:
            if i >= len(s) and j >= len(p): return True
            # if pattern exchausted first and s remaining
            if j >= len(p): return False

            # cache case
            if (i, j) in dp: return dp[(i, j)] 

            # check if matching
            match = (i < len(s) and (s[i] == p[j] or p[j] == '.'))

            # check if there is a char with start (coming next)
            if (j + 1) < len(p) and p[j + 1] == '*':
                use_star = match and dfs(i + 1, j) # use star only if matching
                dont_use_star = dfs(i, j + 2)
                dp[(i, j)] = use_star or dont_use_star
                return dp[(i, j)]

            # if there's no star and this is the last character
            elif match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return dp[(i, j)]
        
        return dfs(0, 0)

        