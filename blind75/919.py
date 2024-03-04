from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # # Write your code here
        # starts = sorted([i.start for i in intervals])
        # ends = sorted([i.end for i in intervals])
        # c, e, s = 0, 0, 0
        # res = -1
        # while s < len(intervals):
        #     if starts[s] < ends[e]:
        #         s += 1
        #         c += 1
        #     else:
        #         e += 1
        #         c -= 1
            
        #     res = max(res, c)

        # heap implemention: earliest ending meeting should be at top
        import heapq
        intervals.sort(key=lambda x: x.start)
        rooms = 1
        q = [intervals[0].end] # start a meeting
        for i in range(1, len(intervals)): # process meetings based on time
            if intervals[i].start < q[0]:
                rooms += 1
            else:
                heapq.heappop(q) # remove completed meeting
            
            heapq.heappush(q, intervals[i].end) # add latest meeting

        return rooms

                