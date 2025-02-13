class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # pattern
        # right -> down -> left -> up
        # [0, 1] -> [1, 0] -> [0, -1] -> [-1, 0]

        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        diPtr = 0

        r, c = 0, 0
        res = [matrix[0][0]]
        matrix[0][0] = "V" # mark as Visited

        while len(res) < ROWS * COLS:
            candr, candc = r + directions[diPtr%4][0], c + directions[diPtr%4][1]

            # invalid element: out of bound, visited
            if (candr < 0 or candr >= ROWS or candc < 0 or candc >= COLS 
                or matrix[candr][candc] == "V"):
                diPtr += 1
                continue
            # valid element
            res.append(matrix[candr][candc])
            matrix[candr][candc] = "V"
            r, c = candr, candc


        return res