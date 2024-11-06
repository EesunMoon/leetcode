class UnionFind:
    def __init__(self, grid):
        self.count = 0
        m,n = len(grid), len(grid[0])
        self.root = []
        self.rank = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.root.append(i*n+j)
                    self.count +=1
                else:
                    self.root.append(-1)
                self.rank.append(0)
    def find(self, i):
        if self.root[i]!=i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1
            self.count -=1
    def getCount(self):
        return self.count

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        nr, nc = len(grid), len(grid[0])
        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] == "0" # Flag to find
                    if r-1 >=0 and grid[r-1][c] == "1":
                        uf.union(r*nc+c, (r-1)*nc+c)
                    if r+1 <nr and grid[r+1][c]=="1":
                        uf.union(r*nc+c, (r+1)*nc+c)
                    if c-1 >=0 and grid[r][c-1] == "1":
                        uf.union(r*nc+c, r*nc+c-1)
                    if c+1 < nc and grid[r][c+1]=="1":
                        uf.union(r*nc+c, r*nc+c+1)
        return uf.getCount()