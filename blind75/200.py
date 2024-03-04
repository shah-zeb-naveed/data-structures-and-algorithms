class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        # bfs
        ROWS, COLS = len(grid), len(grid[0])
        n_islands = 0
        visited = set()

        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                for r_dir, c_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    n_r, n_c = r + r_dir, c + c_dir
                    if n_r < 0 or n_c < 0 or n_r >= ROWS or n_c >= COLS or grid[n_r][n_c] == '0' or (n_r, n_c) in visited:
                        continue
                    q.append((n_r, n_c))
                    visited.add((n_r, n_c))

            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    n_islands += 1
        
        return n_islands
        



        

    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        n_islands = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == '0':
                return 
            
            visited.add((r, c))

            for neib in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                n_r, n_c = neib[0], neib[1]
                dfs(n_r, n_c)
            

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    n_islands += 1
        
        return n_islands
        