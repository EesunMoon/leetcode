class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 # visited
            return (1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    curArea = dfs(r,c)
                    maxArea = max(maxArea, curArea)
        return maxArea
            