class UnionFind():
    def __init__(self, n, edges):
        self.size = n
        self.edges = edges
        self.root = [i for i in range(self.size)]
        self.rank = [0] * n
    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx!=rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1
    def isSameRoot(self, x, y):
        return self.find(x)==self.find(y)
        
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        uf = UnionFind(n, edges)
        
        for x, y in edges:
            uf.union(x, y)
        
        return uf.isSameRoot(source, destination)

        