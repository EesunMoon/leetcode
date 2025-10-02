class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        if ROWS == 0 and COLS == 0:
            return False
        
        c, r = 0, ROWS-1

        while c < COLS and r >=0:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False

