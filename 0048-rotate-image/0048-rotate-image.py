class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        # top l -> top r -> bott r -> bott l
        # (0, 0) -> (0, 4) -> (4, 4) -> (4, 0)
        # (0, 1) -> (1, 4) -> (4, 3) -> (3, 0)

        # (1, 1) -> (3, 1) -> (3, 3) -> (1, 3) # l = 1, r = 3
        while l<r:
            for c in range(r-l):
                tmp = matrix[l][l+c] # top left
                matrix[l][l+c] = matrix[r-c][l] # bottom left
                matrix[r-c][l] = matrix[r][r-c] # bottom right
                matrix[r][r-c] = matrix[l+c][r] # top right
                matrix[l+c][r] = tmp
            r -= 1
            l += 1 
