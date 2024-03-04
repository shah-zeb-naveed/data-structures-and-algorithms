class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        min_triplet = 0
        
        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                triplet_sum = nums[i] + nums[l] + nums[r]                    
                if triplet_sum == target:
                    return triplet_sum
                elif triplet_sum < target:
                    l += 1
                else:
                    r -= 1
                
                diff = abs(triplet_sum - target)
                if diff < min_diff:
                    min_diff = diff
                    min_triplet = triplet_sum

        return min_triplet
            
            