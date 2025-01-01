class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Space O(1), Time O(m*n)
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroRow = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                
                    if r == 0:
                        zeroRow = True
                    else:
                        matrix[r][0] = 0

        # convert element except for first row/col
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # convert first col
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # convert first row
        if zeroRow:
            for c in range(COLS):
                matrix[0][c] = 0
        
        