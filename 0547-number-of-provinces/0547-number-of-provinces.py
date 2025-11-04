class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # DFS
        n = len(isConnected)
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei, connected in enumerate(isConnected[node]):
                if connected and nei not in seen:
                    dfs(nei)
        
        provinces = 0
        for node in range(n):
            if not node in seen:
                dfs(node)
                provinces += 1

        return provinces
        
        """ Union Find TC O(N**2) SC O(N)
        n = len(isConnected) # num of nodes
        # TC O(N**2) SC O(N), N: num of nodes
        parent = [i for i in range(n)] # O(V)
        rank = [1] * n # O(V)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return 0
            if rank[par1] > rank[par2]: # want to combine based on par1
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            return 1
        
        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res -= union(i,j)
        return res
        """