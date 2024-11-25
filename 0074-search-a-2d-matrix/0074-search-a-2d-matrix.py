class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS*COLS-1

        while l<=r:
            m = l + ((r-l)//2)

            # row: m//COLS, col: m%COLS
            cand = matrix[m//COLS][m%COLS]
            if cand == target:
                return True
            elif cand > target:
                r = m-1
            else:
                l = m+1
        return False