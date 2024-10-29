class Solution(object):
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        RootX = self.find(x)
        RootY = self.find(y)

        if RootX != RootY:
            if self.root[RootX] > self.root[RootY]:
                self.root[RootY] = RootX
            elif self.root[RootX] < self.root[RootY]:
                self.root[RootX] = RootY
            else:
                self.root[RootX] = RootY
                self.rank[RootY] += 1

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        self.rank = [1] * n
        self.root = [i for i in range(n)]
        num = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1 and self.find(i) != self.find(j):
                    num -= 1
                    self.union(i, j)
                    print(self.root)

        return num