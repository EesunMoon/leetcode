class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
        self.cc = n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra==rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        self.cc -= 1
        return True

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n <= k:
            return 0
        edges_sorted = sorted(edges, key=lambda x:x[2])
        dsu=DSU(n)
        for u, v, w in edges_sorted:
            if dsu.union(u, v):
                if dsu.cc <=k:
                    return w
        return 0