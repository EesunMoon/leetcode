class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(set)
        colHash = defaultdict(set)
        boxHash = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                if ((board[r][c] in rowHash[r]) 
                    or (board[r][c] in colHash[c]) 
                    or (board[r][c] in boxHash[(r//3, c//3)])):
                    return False
                rowHash[r].add(board[r][c])
                colHash[c].add(board[r][c])
                boxHash[(r//3, c//3)].add(board[r][c])
        
        return True