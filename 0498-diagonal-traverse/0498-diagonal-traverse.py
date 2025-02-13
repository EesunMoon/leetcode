class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        3 x 4

        (0, 0) -> 
        (0, 1), (1, 0) -> 
        (2, 0), (1, 1), (0, 2) -> 
        (0, 3), (1, 2), (2, 1) ->
        (2, 2), (3, 1) ->
        (2, 3)

        [diagonal set pattern] sumDiag - Outer loop
        0 -> 1 -> 2 -> 3 -> 4 -> 5
            (3-1=2)+(4-1=3) = 5
        [each diagonal set pattern] - inner loop
        sumDiag, 0 -> sumDiag-1, 0+1 -> ... -> 0, sumDiag
        """
        res = []
        ROWS, COLS = len(mat), len(mat[0]) # final: (ROWS-1 + COLS-1)
        final = (ROWS-1)+(COLS-1)
        direc = True # True: Row -> Col, False: Col -> Row


        for sumDiag in range(0, final+1):
            if direc:
                row, col = sumDiag, 0
                while True:
                    ## invalid
                    # starting point
                    if row >= ROWS:
                        row -= 1
                        col += 1
                        continue
                    # ending point
                    if row < 0 or col >= COLS:
                        direc = not direc
                        break
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                row, col = 0, sumDiag
                while True:
                    ## invalid
                    # starting point
                    if col >= COLS:
                        row += 1
                        col -= 1
                        continue
                    # ending point
                    if row >=ROWS or col < 0:
                        direc = not direc
                        break
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
        return res