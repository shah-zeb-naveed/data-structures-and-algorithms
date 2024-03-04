class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_max = 1
        cur_min = 1
        res = max(nums)

        for num in nums:
            if num == 0:
                cur_min = 1
                cur_max = 1
                continue
                
            num_max = num * cur_max # 2, 6, -12, -8
            num_min = num * cur_min # 2, 6, -5, -48
            
            cur_max = max(num_min, num_max, num) # 2, 6, -2, 4
            cur_min = min(num_min, num_max, num) # 2, 3, -12, -48
            
            res = max(res, cur_max) # 4, 6, 6, 6

        return res # 6
            
        