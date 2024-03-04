class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        suff = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]

        return ans
        
        # cum_sum = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     cum_sum *= nums[i]
        #     suff[i] = cum_sum

        # for i in range(len(nums)):
        #     if i == 0:
        #         ans[i] = suff[i + 1]
        #     elif i == len(nums) - 1:
        #         ans[i] = pre[i - 1]
        #     else:
        #         ans[i] = pre[i - 1] * suff[i + 1] 

        return ans
        

        