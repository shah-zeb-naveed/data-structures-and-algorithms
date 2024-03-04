class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start <= last_end:
                res[-1][1]= max(res[-1][1], end)
                # res.pop()
                # res.append(merged)
            else:
                res.append([start, end])
    
        return res
        