class Solution:
    # narrow down to that middle element that will be mid point
    # search based on where in slope
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:

            if nums[l] < nums[r]: # equality not required
                return min(res, nums[l])

            m = (l + r) // 2
            res = min(nums[m], res)
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
        