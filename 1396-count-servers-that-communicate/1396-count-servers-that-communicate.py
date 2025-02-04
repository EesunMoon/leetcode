class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # use two array - represent row, col index that have server
        ROWS, COLS = len(grid), len(grid[0])
        rowIdx, colIdx = [0] * ROWS, [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rowIdx[r] += 1
                    colIdx[c] += 1
        
        # rowIdx, colIdx >1 : except for itself
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (rowIdx[r] > 1 or colIdx[c] > 1) and (grid[r][c] == 1):
                    res += 1

        return res