class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DT Method 1: add or not add and keep accumulating sum
        # DT Method 2: track remaining sum given an index and use memoization
        # O (N * SUMS(N)), O (N * SUMS(N))
        # Array bottom up: add current to possible sums of next elements. Start from end. 
        # O (N * SUMS(N)), O (SUMS(N))
    
        total = sum(nums)
        if total % 2 != 0: return False
        dp = set([0])

        for i in range(len(nums) - 1, -1, -1):
            for sums in list(dp):
                # add sum with possiblity of current numn included. current excluded
                # already calculated (partially yet and its calculation will be completed
                # in next iterations
                dp.add(sums + nums[i])

        return total // 2 in dp
    
        # 1, 5, 11, 5
        # 0
        # 5 -> 0, 5
        # 11 -> 0, 5, 11, 16
        # 5 -> 0, 5, 11, 16, 21
        # 1 -> 0, 5, 11, 16, 21, 17, 22
