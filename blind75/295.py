class MedianFinder:

    def __init__(self):
        import heapq
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # always first push to small
        heapq.heappush(self.small, -num)

        # make sure small is small
        if self.small and self.large and (-self.small[0] > self.large[0]):
            popped = -heapq.heappop(self.small)
            heapq.heappush(self.large, popped)

        # size adjustment.
        if len(self.small) > len(self.large) + 1:
            popped = -heapq.heappop(self.small)
            heapq.heappush(self.large, popped)
        if len(self.large) > len(self.small) + 1:
            popped = heapq.heappop(self.large)
            heapq.heappush(self.small, -popped)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]    
        else:
            return ((-self.small[0]) + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()