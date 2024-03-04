class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # o(n) - greedy
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return goal == 0

        # o(n^2)
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = False
            # i = 2
            for j in range(i + 1, i + nums[i] + 1): # (3, 3 + 1)
                #print(i, j, nums[i])
                dp[i] = dp[i] or dp[j]
                if dp[i] == True: # without this optimization, time limit exceeds
                    break
        
        return dp[0]
        