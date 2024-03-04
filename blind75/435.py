class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        r = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            # no overlap
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            else:
                prev_end = min(intervals[i][1], prev_end)
                r +=  1

        return r