class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if r in (-1, ROWS) or c in (-1, COLS) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))

        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(dfs(r, c), maxArea)

        return maxArea
        