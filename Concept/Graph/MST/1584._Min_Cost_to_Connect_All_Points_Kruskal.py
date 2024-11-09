# check the cycle
class UnionFind():
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx]+=1
        return True

import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def man_dist(p1, p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        
        n = len(points)
        dist_info = []

        for i in range(n-1):
            for j in range(i+1, n):
                dist_info.append((man_dist(points[i],points[j]), i, j))

        # sorted with ascending order
        heapq.heapify(dist_info)
        # dist_info.sort() 
        print(dist_info)

        edge_limited = 0 # until n-1
        total_weight = 0
        uf = UnionFind(n)

        while dist_info or edge_limited != n-1:
            weight, p1, p2 = heapq.heappop(dist_info)
            if uf.union(p1, p2):
                total_weight += weight
                edge_limited += 1
        
        return total_weight
