class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # unique answer doens't mean the individual frequencies will never be the same

        # counter dict
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Method 1: O(n) using hashmap and lists
        # convert to bucket array
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in freq.items():
            buckets[c].append(n)
            
        # linear scan
        res = []
        for i in reversed(range(len(buckets))):
            for j in buckets[i]:
                if len(res) == k: break
                res.append(j)
        
        # Method 2:

        # import heapq
        # q = []
        # # O(N)
        # for r, c in freq.items():
        #     q.append((-c, r)) # convert to max heap
        
        # # O(N)
        # heapq.heapify(q) # inplace I guess

        # res = []
        # # K LOG N
        # while len(res) < k:
        #     el = heapq.heappop(q)[1]
        #     res.append(el)
        
        return res