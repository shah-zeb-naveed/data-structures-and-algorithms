class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # CHATGPT MEMOIZAITON VERSION. FAR MORE EFFICIENT
        
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Initialize the DP table
        dp = [[0] * n for _ in range(n)]
        
        # Iterate over all possible interval lengths
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                # Iterate over all possible choices of the last balloon to burst in the interval
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        
        # The result is stored in dp[0][n-1]
        return dp[0][n-1]

    def maxCoins1(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        # O(N^2)
        def dfs(l, r):
            # base: single element sub-array allowed
            if l > r: return 0 

            # cache
            if (l, r) in dp: return dp[(l, r)]

            # recursion and save cache
            # ith element burst last
            for i in range(l, r + 1):
                coins = 0
                # at the end, left and right would be gone so look outside the range
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # now recurse to the neighbors who go first
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp.get((l, r), 0), coins)
            return dp[(l, r)]
        return dfs(1, len(nums) - 2) 