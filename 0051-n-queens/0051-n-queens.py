class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col, posDiag, negDiag = set(), set(), set() # posDiag: (r+c), negDiag: (r-c)

        board = [["."]*n for _ in range(n)]
        res = []

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                # add
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtracking(r+1) # next row

                # clean up
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtracking(0)
        return res