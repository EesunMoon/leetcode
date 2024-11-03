class Solution(object):
    def __init__(self):
        self.cache = {}
    def Pascal(self, i, j):
        
        if (i, j) in self.cache:
            return self.cache[(i, j)]

        # base case
        if j == 0 or j==i:
            return 1
        else:
            result = self.Pascal(i-1, j-1) + self.Pascal(i-1, j)
        
        self.cache[(i, j)] = result
        return self.cache[(i, j)]
        
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        answer = []

        for i in range(rowIndex+1):
            answer.append(self.Pascal(rowIndex,i))
        
        return answer