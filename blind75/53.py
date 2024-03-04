class Solution:
    def maxCrossingSum(self, arr, l, m, h): 
    
        # Include elements on left of mid and mid
        sm = 0
        left_sum = float('-inf')
    
        for i in range(m, l-1, -1): 
            sm += arr[i] 
            left_sum = max(left_sum, sm) 
    
        # Include elements on right of mid and mid
        sm = 0
        right_sum = float('-inf')
        for i in range(m, h + 1): 
            sm += arr[i] 
            right_sum = max(sm, right_sum) 

        return max(left_sum + right_sum - arr[m], left_sum, right_sum)
    
    
    # Returns sum of maximum sum subarray in aa[l..h] 
    def maxSubArraySum(self, arr, l, h): 
        # #Invalid Range: low is greater than high 
        # if (l > h): 
        #     return float(-inf)
        # Base Case: Only one element 
        if (l >= h): 
            return arr[l] 
    
        # Find middle point 
        m = (l + h) // 2
    
        # Return maximum of following three possible cases 
        # a) Maximum subarray sum in left half 
        # b) Maximum subarray sum in right half 
        # c) Maximum subarray sum such that the 
        #     subarray crosses the midpoint

        l_sum = self.maxSubArraySum(arr, l, m-1)
        r_sum = self.maxSubArraySum(arr, m+1, h)
        c_sum = self.maxCrossingSum(arr, l, m, h)
        
        print(l_sum, r_sum, c_sum)

        return max(l_sum, r_sum, c_sum) 

    def maxSubArray1(self, nums: List[int]) -> int:
        if low == high:
            return nums[low]

        mid = (low + high) // 2
        left_max = find_max_subarray(nums, low, mid)
        right_max = find_max_subarray(nums, mid + 1, high)

        # Calculate maximum crossing subarray sum
        left_sum, right_sum = 0, 0
        max_crossing_sum = float('-inf')
        for i in range(mid, low - 1, -1):
            left_sum = max(left_sum, nums[i] + left_sum) # max(4, 3) # 
            max_crossing_sum = max(max_crossing_sum, left_sum)

        for i in range(mid + 1, high + 1):
            right_sum = max(right_sum, nums[i] + right_sum)
            max_crossing_sum = max(max_crossing_sum, right_sum + left_sum)

        return max(left_max, right_max, max_crossing_sum)
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        return self.maxSubArraySum(nums, 0, len(nums)-1) 

        max_sum = float(-inf)
        cur_sum = 0
        for num in  nums:
            cur_sum = max(cur_sum, 0) # reset if negative
            cur_sum += num
            max_sum = max(cur_sum, max_sum)

        return max_sum


        
        