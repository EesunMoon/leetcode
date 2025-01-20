class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])

        visited = set()
        def backtracking(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS 
                or (r, c) in visited or board[r][c] != word[i]):
                return False
            
            visited.add((r, c))
            res = (backtracking(r+1, c, i+1) or
                    backtracking(r-1, c, i+1) or
                    backtracking(r, c+1, i+1) or
                    backtracking(r, c-1, i+1))
            visited.remove((r,c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtracking(r, c, 0):
                    return True
        return False