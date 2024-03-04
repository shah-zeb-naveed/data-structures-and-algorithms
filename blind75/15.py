class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # can do two sum but apply two sum II approach i.e. with sorted array, use pointers

        nums.sort()
        results = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
        
            while l < r:
                triplet_sum = num + nums[l] + nums[r]

                if triplet_sum > 0:
                    r -= 1
                elif triplet_sum < 0:
                    l += 1
                else:
                    results.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return results

