class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = []
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = 0, 0
        flag = 0
        cnt = 0

        while cnt < ROWS * COLS:
            ans.append(matrix[r][c])
            matrix[r][c] = "X"
            cnt += 1
            candr, candc = r + directions[flag][0], c + directions[flag][1]

            if candr in (-1, ROWS) or candc in (-1, COLS) or matrix[candr][candc] == "X":
                flag = (flag+1)%4
    
            r += directions[flag][0]
            c += directions[flag][1]

        return ans