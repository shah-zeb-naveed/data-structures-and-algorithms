class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search starts with left and right pointers
        # and almost halving input range
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left sorted portion: technically
            # we mean that there is no pivot between left and mid
            if nums[l] <= nums[mid]:
                if nums[mid] < target:
                    l = mid + 1
                elif target < nums[l]: # 0 < 0 false
                    l = mid + 1 # would cross 0
                else: # 0 = 0
                    r = mid - 1 # point r towards 0
                
                # SHOULD'VE THOUGHT ABOUT TARGET == NUMS[L]
                # L IS THE REFERENCE POINT
                # elif target > nums[l]: # 0 > 0 -> false
                #     r = mid - 1 # would point r towards 0
                # else:
                #     l = mid + 1 # would cross 0

            # right sorted portion
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1