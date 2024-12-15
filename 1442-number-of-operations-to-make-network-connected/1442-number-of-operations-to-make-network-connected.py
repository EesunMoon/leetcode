class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        V = len(connections)

        # base case N-1 <= V
        if V < n-1:
            return -1
        
        # initialize
        # adj = defaultdict(list)
        # for e, v in connections:
        #     adj[e].append(v)
        #     adj[v].append(e)
    
        par = [i for i in range(n)]
        rank = [1] * n
        self.count = n
        
        def find(node):
            p = par[node]
            while p!=par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 != p2:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
                self.count -= 1 # component
        
        for u, v in connections:
            union(u, v)
        
        return self.count - 1