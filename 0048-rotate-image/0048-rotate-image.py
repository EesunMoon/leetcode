class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # set left/right boundary
        l, r = 0, len(matrix)-1

        while l<r:
            # move element 
            for i in range(r-l):
                top, bottom = l, r

                # save top-left element
                topleft = matrix[top][l+i]

                # move bottom-left into top-left
                matrix[top][l+i] = matrix[bottom-i][l]

                # move bottom-right into bottom-left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # move top-right into bottom-right
                matrix[bottom][r-i] = matrix[top+i][r]

                # move top-left into top-right
                matrix[top+i][r] = topleft
            
            # move left, right pointers
            l += 1
            r -= 1
        