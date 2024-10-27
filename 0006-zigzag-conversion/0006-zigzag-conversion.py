class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if not s:
            return ""
        if len(s) == 1 or numRows >= len(s) or numRows == 1:
            return s
        
        zigzag = [''] *(numRows)
        direct = 0
        row = 0

        for x in s:
            if direct == 0:
                zigzag[row] += x
                if row == numRows-1: # last
                    if numRows != 2:
                        direct = 1
                    row -=1
                    continue
                row += 1
            elif direct == 1:
                zigzag[row] += x
                if row == 1:
                    direct = 0
                row -= 1
        print(zigzag)

        return ''.join(zigzag)
        