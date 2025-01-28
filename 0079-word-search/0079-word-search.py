class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        seen = set()
        # back tracking
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in seen or board[r][c] != word[idx]):
                return False
            
            seen.add((r, c))
            res = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) 
                    or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))
            seen.remove((r, c))
            return res
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False