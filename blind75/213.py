class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums, i, j):

            rob1, rob2 = 0, 0

            for k in range(i, j + 1, 1):
                temp = max(nums[k] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        left_rob = helper(nums, 0, len(nums) - 2)
        right_rob = helper(nums, 1, len(nums) - 1)

        return max(nums[0], left_rob, right_rob)
    
        