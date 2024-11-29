class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        flag = 0
        res = []
        seen = set()
        r, c = 0, 0

        # start
        seen.add((0,0))
        res.append(matrix[0][0])

        while len(seen) < ROWS*COLS:
            candr = r + directions[flag][0]
            candc = c + directions[flag][1]
            
            if (candr, candc) in seen or not (0 <= candr < ROWS and 0 <= candc < COLS):
                flag = (flag+1)%4
                continue
            r, c = candr, candc
            res.append(matrix[r][c])
            seen.add((r,c))

        
        return res
        