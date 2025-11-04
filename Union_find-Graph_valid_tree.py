class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1==p2:
            return False # cycle, already merged
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = self.parent[p2]
            self.rank[p2] += self.rank[p1]
        return True 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. no cycles
        # -> num edges == n-1
        # -> if num edges >= n --> cycle
        # ->              < n-1 --> seperate component
        # -> cycle detection: has same parent
        # 2. all node connected
        # -> check total componenet == 1
        if len(edges)!=n-1:
            return False
        
        dsu = DSU(n)
        for n1, n2 in edges:
            if not dsu.union(n1, n2):
                return False
        return True

