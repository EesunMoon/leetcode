class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        # 1) [DFS] unsurrounding "O" -> "V"
        def dfs(r, c):
            # base case
            if r in (-1, ROWS) or c in (-1, COLS) or board[r][c] != "O":
                return
            board[r][c] = "V"
            
            # direction
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and r in [0, ROWS-1] or c in [0, COLS-1]:
                    dfs(r, c)

        # 2) "O" -> "X": O(n*m)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3) "V" -> "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "V":
                    board[r][c] = "O"
        