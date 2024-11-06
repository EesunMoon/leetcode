class Solution(object):
    def dfs(self, grid, r, c):
        if r in (-1, self.m) or c in (-1, self.n) or grid[r][c] != "1":
            return
        
        grid[r][c] = "0"
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        num_islands = 0
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1
        return num_islands
