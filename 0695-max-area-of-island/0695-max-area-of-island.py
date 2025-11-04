class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 # visited
            cnt = 1
            for dr, dc in directions:
                cnt += dfs(dr+r, dc+c)
            return cnt

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    curArea = dfs(r,c)
                    maxArea = max(maxArea, curArea)
        return maxArea
            