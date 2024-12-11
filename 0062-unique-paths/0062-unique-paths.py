class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n # last row

        for i in range(m-1):
            currRow = [1] * n
            for j in range(n-2, -1, -1):
                currRow[j] = currRow[j+1] + row[j]
            row = currRow
        return row[0]
