class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # base case
        if not matrix:
            return False

        n, m = len(matrix), len(matrix[0])
        row, col = 0, m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col-=1
            else:
                row+=1

        return False

        