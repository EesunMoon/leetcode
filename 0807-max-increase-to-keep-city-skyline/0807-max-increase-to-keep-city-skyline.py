class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRow = [max(grid[r]) for r in range(n)]
        maxCol = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        res = 0
        for r in range(n):
            for c in range(n):
                res += (min(maxRow[r], maxCol[c]) - grid[r][c])
                
        return res