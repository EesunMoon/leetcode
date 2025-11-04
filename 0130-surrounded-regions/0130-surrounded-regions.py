class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        # 1. unsurrounded portion: O -> T
        def dfs(r, c):
            if (r<0 or r>=m or c<0 or c>=n or board[r][c]!="O"):
                return
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for r in range(m):
            for c in range(n):
                if r == 0 or r==m-1 or c==0 or c==n-1 and board[r][c] == "O":
                    dfs(r, c)

        # 2. surrounded portion: O -> X
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. reverse: T -> O
        for r in range(m):
            for c in range(n):
                if board[r][c] == "T":
                    board[r][c] = "O"