class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0011
        # 0000
        # 0001
        # 0100
        # 0010

        # xor all numbers and then xor with nums -> remaining will be missing
        # or just subtract sum in a single pass

        # 3 0 1 (4)
        # 0 1 2 (3)
        # 3 -1 -1 (1)


        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res