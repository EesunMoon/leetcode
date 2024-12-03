class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        par = [i for i in range(n)]
        rank = [1]*n

        def find(node):
            p = par[node]
            
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            else:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
            
            return True
        
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        
        return res