class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            if (r in (-1, ROWS) or c in (-1, COLS) or grid[r][c] == 0 or (r, c) in seen):
                return 0
            
            if grid[r][c] == 1:
                seen.add((r, c))
                return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        maximum = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maximum = max(maximum, dfs(r, c))

        return maximum
        