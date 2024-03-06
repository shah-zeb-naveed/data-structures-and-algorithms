class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # only need to track 2 rows, not entire 2D
        # can skip last row and last column
    
        next_row = [1] * n
        for _ in range(m - 1): # don't run for last row
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + next_row[j]

            next_row = new_row

        return next_row[0]            
        