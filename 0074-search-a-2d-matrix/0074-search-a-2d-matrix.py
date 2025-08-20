class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ 4 x 3 = m x n
        [0,0] [0,1] [0,2] 0 1 2 [0//n, 0%n]
        [1,0] [1,1] [1,2] 3 4 5
        [2,0] [2,1] [2,2] 6 7 8
        [3,0] [3,1] [3,2] 9 10 11

        3 x 4 = m x n
        [0,0] [0,1] [0,2] [0,3] 0 1 2 3 [0//n, 0%n]
        [1,0] [1,1] [1,2] [1,3] 4 5 6 7
        [2,0] [2,1] [2,2] [2,3] 8 9 10 11
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n-1
        while l<=r:
            middle = (l+r)//2
            cand = matrix[middle//n][mod(middle, n)]
            if target == cand:
                return True
            elif target > cand: # right boundary
                l = middle+1
            else: # left boundary
                r = middle-1

        return False