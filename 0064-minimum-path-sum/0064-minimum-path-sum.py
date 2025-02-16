class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        1 4 5
        2 (5+2, 5+4)
        dp[i, j] = grid[i, j] + min(dp[i+1,j], dp[i, j+1])
        """
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if r == ROWS-1 and c != COLS-1:
                    dp[r][c] = grid[r][c] + dp[r][c+1]
                elif r != ROWS-1 and c == COLS-1:
                    dp[r][c] = grid[r][c] + dp[r+1][c]
                elif r!= ROWS-1 and c != COLS-1:
                    dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
                else:
                    dp[r][c] = grid[r][c]
        return dp[0][0]