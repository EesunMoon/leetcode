class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        ROWS, COLS = len(grid),len(grid[0])
        # visited = set()

        def dfs(r, c):
            if r in (-1, ROWS) or c in (-1, COLS) or grid[r][c] == 0:
                return 0
            # visited.add((r, c))
            grid[r][c] = 0
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r, c), maxArea)
        
        return maxArea
                
        