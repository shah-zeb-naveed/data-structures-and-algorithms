class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        next_row = [1] * n
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + next_row[j]

            next_row = new_row

        return next_row[0]            
        