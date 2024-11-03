class Solution(object):
    def getRow(self, rowIndex):
        cache = {}
        def Pascal(i, j):
            # base case
            if j == 0 or j==i:
                return 1
            if (i, j) not in cache:
                cache[(i, j)] = Pascal(i-1, j-1) + Pascal(i-1, j)
            
            return cache[(i, j)]
        
        answer = []
        for i in range(rowIndex+1):
            answer.append(Pascal(rowIndex,i))
        
        return answer