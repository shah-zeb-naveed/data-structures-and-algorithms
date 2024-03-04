class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:
            return []

        def check_sum_recursive(nums, i, k):
            if k == 2:
                l, r = i, len(nums) - 1
                while l < r:
                    q_sum =  sum(test) + nums[l] + nums[r]
                    if q_sum < target:
                        l += 1
                    elif q_sum > target:
                        r -= 1
                    else:
                        results.append([test[0], test[1], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                return

            j = i
            while j <= (len(nums) - 1) - (k - 1):

                # skip duplicates
                if j > i and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                # recurse
                test.append(nums[j])
                print('test:', test)
                check_sum_recursive(nums, j+1, k-1)

                # backtrack
                test.pop()
                j += 1

        nums.sort()
        print('sorted: ', nums)
        results = []
        test = []
        check_sum_recursive(nums, i=0, k=4)
        return results
            
        