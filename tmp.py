from queue import PriorityQueue
from heapq import heapify, heappush, heappop

class Solution:

    def get_dist_sq(self, point):
        return pow(point[0], 2) + pow(point[1], 2)

    def partition_by_middle_2(self, points, left, right):
        piv_idx = (left + right) // 2
        pivot = self.get_dist_sq(arr[piv_idx])

        arr[piv_idx], arr[right] = arr[right], arr[piv_idx]

        print('Pivot: ', pivot, ', right: ', right)

        for j in range(left, right):
            print(list(map(self.get_dist_sq, points)), 'left, j', left, j)

            # all the elements smaller or equal to pivot will be to the left
            if self.get_dist_sq(points[j]) <= pivot: 
                arr[left], arr[j] = arr[j], arr[left]
                left += 1

        arr[left], arr[right] = arr[right], arr[left]
        print(list(map(self.get_dist_sq, points)))
        return left

    def partition(self, points, left, right):
        
        pivot = self.choose_pivot(points, left, right)
        print('Pivot: ', pivot)
        
        while left < right:
            print(points, list(map(self.get_dist_sq, points)))
            if self.get_dist_sq(points[left]) >= pivot:
                print('Swapping')
                points[left], points[right] = points[right], points[left]
                right -= 1
            
            else:
                left += 1

        # Once the two pointers meet, we'll need to make sure the left pointer has completely moved past the end of the left side partition, then we can return it back to the QuickSelect function as the pivotIndex representing the left-most edge of the right partition.
    
        if self.get_dist_sq(points[left]) < pivot:
            left += 1

        print(points, list(map(self.get_dist_sq, points)))
        print('------------------------------------------')   
        return left        

    def quick_select(self, points, k):
        
        left, right = 0, len(points) - 1
        pivot = len(points) # just a placeholder
        
        while pivot != k:
            pivot = self.partition_by_middle_2(points, left, right)
            print('Pivot: ', pivot)
            
            if pivot < k:
                left = pivot # short of elements. need to include this for sure.
            
            else:
                right = pivot - 1 # can safely exclude this one
        
        return points[:k]
    
    def choose_pivot(self, points, left: int, right: int):
        return self.get_dist_sq(points[(right + left) // 2])
        
    def kClosest(self, points, k: int):
        return self.quick_select(points, k)

arr = [[3,3],[5,-1],[-2,4],[-2,5]]
sol = Solution()
rest = sol.kClosest(arr, 3)
        
print(list(map(sol.get_dist_sq, rest)))