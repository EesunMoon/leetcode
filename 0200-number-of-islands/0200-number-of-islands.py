class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def search(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0" # mark as visited

            for dr, dc in directions:
                search(dr+r, dc+c)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    search(r, c)
                    res += 1
        return res